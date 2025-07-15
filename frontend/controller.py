import cv2
import threading
import requests
import numpy as np
import time
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

class ControllerCamera:
    def __init__(self, UI, camera):
        self.UI = UI
        self.camera = camera
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_frame)
        self._connect_signal()
        self.session = requests.Session()  # Reuse TCP connection
        self.running = False

    def _connect_signal(self):
        self.UI.left_sidebar.btn_init_camera.clicked.connect(self._start_camera)
        self.UI.left_sidebar.btn_stop_camera.clicked.connect(self._stop_camera)
        print("[INFO] Camera start button connected")

    def _start_camera(self):
        self.camera._start_camera()
        if self.camera.isCamOpen:
            self.running = True
            self.timer.start(100)
            print("[INFO] Camera started successfully")

    def _stop_camera(self):
        if self.camera.cap and self.camera.isCamOpen:
            self.running = False
            self.camera._stop_camera()
            self.timer.stop()
            self.UI.center_panel.clear()

    def _update_frame(self):
        frame = self.camera._read_frame()
        if frame is not None:
            # ❌ Don't display raw frame
            threading.Thread(target=self._send_async_http, args=(frame,), daemon=True).start()

    def _send_async_http(self, frame):
        try:
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
            response = self.session.post(
                "http://localhost:8000/api/receive_frame/",
                files={"frame": ("frame.jpg", buffer.tobytes(), "image/jpeg")},
                timeout=3.0  # Increased from 1.5 → give server time to respond
            )
            if response.status_code == 200:
                # This ensures the full response body is consumed
                content = response.content
                img = cv2.imdecode(np.frombuffer(content, np.uint8), cv2.IMREAD_COLOR)
                if img is not None:
                    self._display_processed_frame(img)
            else:
                print("[WARN] Server returned", response.status_code)
                time.sleep(0.2)
        except requests.exceptions.ReadTimeout:
            print("[WARN] Timeout waiting for response from server")
        except Exception as e:
            print("[ERROR] Streaming failed:", e)


    def _display_processed_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        img = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        self.UI.center_panel.setPixmap(QPixmap.fromImage(img).scaled(
            self.UI.center_panel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
