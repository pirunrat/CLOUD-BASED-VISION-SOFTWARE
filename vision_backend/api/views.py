from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.core.cache import cache
from django.http import StreamingHttpResponse, HttpResponse
import cv2
import numpy as np
import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
def run_model(request):
    input_data = request.data.get('image_data')
    
    if not input_data:
        return Response({"error": "No image_data provided"}, status=400)

    # Check cache
    cached = cache.get(input_data)
    if cached:
        return Response({"result": cached, "source": "cache"})

    try:
        response = requests.post("http://localhost:8001/infer", json={"image_data": input_data}, timeout=5)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.RequestException as e:
        logger.error("FastAPI inference failed: %s", e)
        return Response({"error": "Inference backend unreachable"}, status=500)

    # Cache and return
    cache.set(input_data, result, timeout=300)
    return Response({"result": result, "source": "model"})


# --------------------------------------------- Video Stream --------------------------------------------- #

def generate_frames():
    cap = cv2.VideoCapture(0)
    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    except (ConnectionResetError, BrokenPipeError):
        logger.info("Client disconnected from video stream.")
    except Exception as e:
        logger.exception("Error during video streaming: %s", e)
    finally:
        cap.release()


@api_view(['GET'])
def video_stream(request):
    try:
        return StreamingHttpResponse(
            generate_frames(),
            content_type='multipart/x-mixed-replace; boundary=frame'
        )
    except Exception as e:
        logger.error("StreamingHttpResponse error: %s", e)
        return HttpResponse("Streaming error", status=500)


# --------------------------------------------- Object Detection --------------------------------------------- #

@api_view(['POST'])
def receive_frame(request):
    if 'frame' not in request.FILES:
        return HttpResponse("No frame provided", status=400)

    try:
        frame_file = request.FILES['frame']
        nparr = np.frombuffer(frame_file.read(), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img_np is None:
            return HttpResponse("Invalid image", status=400)

        success, img_encoded = cv2.imencode('.jpg', img_np)
        if not success:
            return HttpResponse("Image encoding failed", status=500)

        image_bytes = img_encoded.tobytes()

        response = requests.post("http://localhost:8001/infer", files={"image": image_bytes}, timeout=5)
        response.raise_for_status()
        boxes = response.json().get("boxes", [])

        for box in boxes:
            x, y, w, h = box['bbox']
            label = box['label']
            cv2.rectangle(img_np, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img_np, label, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        success, final_image = cv2.imencode('.jpg', img_np)
        if not success:
            return HttpResponse("Final encoding failed", status=500)

        try:
            return HttpResponse(final_image.tobytes(), content_type='image/jpeg')
        except BrokenPipeError:
            logger.warning("Client closed connection before receiving the image.")
            return HttpResponse(status=499)

    except requests.exceptions.RequestException as e:
        logger.error("FastAPI error during object detection: %s", e)
        return HttpResponse("Object detection failed", status=502)
    except Exception as e:
        logger.exception("Unexpected error in receive_frame: %s", e)
        return HttpResponse("Internal server error", status=500)
