from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from ultralytics import YOLO
from fastapi.responses import JSONResponse

app = FastAPI()
model = YOLO("yolov8n.pt")  # or yolov8s.pt / your custom model

@app.post("/infer")
async def infer(image: UploadFile = File(...)):
    contents = await image.read()
    np_arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(img, verbose=False)
    boxes = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = model.names[int(box.cls[0])]
            boxes.append({"label": label, "bbox": [x1, y1, x2 - x1, y2 - y1]})

    return JSONResponse(content={"boxes": boxes})
