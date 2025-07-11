from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
from django.core.cache import cache
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from django.http import HttpResponse
import cv2
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




face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@api_view(['POST'])
def receive_frame(request):
    if 'frame' in request.FILES:
        frame_file = request.FILES['frame']
        nparr = np.frombuffer(frame_file.read(), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Step 1: Convert to grayscale
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

        # Step 2: Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Step 3: Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img_np, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Step 4: Encode to JPEG and return
        success, encoded_image = cv2.imencode('.jpg', img_np)
        if success:
            return HttpResponse(encoded_image.tobytes(), content_type='image/jpeg')
        else:
            return HttpResponse("Failed to encode image", status=500)

    return HttpResponse("No frame provided", status=400)




