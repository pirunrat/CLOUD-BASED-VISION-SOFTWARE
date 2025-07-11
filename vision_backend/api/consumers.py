# import cv2
# import numpy as np
# from channels.generic.websocket import AsyncWebsocketConsumer

# class FrameConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         print("✅ WebSocket connected")

#     async def disconnect(self, close_code):
#         print("❌ WebSocket disconnected")

#     async def receive(self, text_data=None, bytes_data=None):
#         if bytes_data:
#             nparr = np.frombuffer(bytes_data, np.uint8)
#             img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#             print("✅ Received frame:", img_np.shape)


import cv2
import numpy as np
from channels.generic.websocket import AsyncWebsocketConsumer
import time

class FrameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("✅ WebSocket connected")

    async def disconnect(self, close_code):
        print("❌ WebSocket disconnected")

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            # Step 1: Decode image
            nparr = np.frombuffer(bytes_data, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            #print("✅ Received frame:", img_np.shape)

            # Step 2: Convert to grayscale
            gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

            # Step 3: Apply Sobel Edge Detection
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            sobel = cv2.magnitude(sobel_x, sobel_y)
            sobel = np.uint8(np.clip(sobel, 0, 255))

            # Step 4: Convert back to BGR (for viewing in color channels)
            sobel_bgr = cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)

            # Step 5: Encode processed image as PNG
            start_time = time.time()
            success, buffer = cv2.imencode('.jpg', sobel_bgr, [cv2.IMWRITE_JPEG_QUALITY, 70])
            if success:
                await self.send(bytes_data=buffer.tobytes())
                print(f"✅ Sent frame in {time.time() - start_time:.3f}s")
                #print("✅ Sent processed frame back")
            else:
                print("❌ Failed to encode processed frame")
