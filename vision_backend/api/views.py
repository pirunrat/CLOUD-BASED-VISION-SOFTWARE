from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
from django.core.cache import cache
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
import numpy as np

import cv2

@api_view(['POST'])
# @permission_classes([IsAuthenticated])  # Uncomment for auth
def run_model(request):
    input_data = request.data.get('image_data')
    
    # Check cache
    cached = cache.get(input_data)
    if cached:
        return Response({"result": cached, "source": "cache"})

    # Forward to FastAPI
    response = requests.post("http://localhost:8001/infer", json={"image_data": input_data})
    result = response.json()

    # Cache the result
    cache.set(input_data, result, timeout=300)

    return Response({"result": result, "source": "model"})


# ------------------------------------------------- Fetch Franes -------------------------------------------#

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    cap.release()

@api_view(['GET'])
def video_stream(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')


@api_view(['POST'])  # ✅ Correct method
def receive_frame(request):
    if 'frame' in request.FILES:
        frame_file = request.FILES['frame']
        nparr = np.frombuffer(frame_file.read(), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # ✅ Do something with the received image
        print("Received frame of shape:", img_np.shape)

        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    
    return Response({'status': 'error', 'message': 'No frame provided'}, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def video_frame(request):
#     """Returns a single JPEG frame from a file or camera"""
#     # Simulate a camera/image read
#     frame = cv2.imread("path/to/sample.jpg")  # or use cv2.VideoCapture() for live feed
#     if frame is None:
#         return Response({"error": "Frame not found"}, status=404)

#     _, buffer = cv2.imencode('.jpg', frame)
#     return Response(buffer.tobytes(), content_type='image/jpeg')
