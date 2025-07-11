# import cv2
# import threading
# import websocket
# from PyQt5.QtCore import QTimer, Qt
# from PyQt5.QtGui import QImage, QPixmap

# class ControllerCamera:
#     def __init__(self, UI, camera):
#         self.UI = UI
#         self.camera = camera
#         self.timer = QTimer()
#         self.timer.timeout.connect(self._update_frame)
#         self._connect_signal()
#         self.frame_counter = 0

#         # WebSocket setup
#         self.ws = None
#         self._init_websocket()

#     def _init_websocket(self):
#         try:
#             self.ws = websocket.WebSocket()
#             self.ws.connect("ws://localhost:8000/ws/stream/")
#             print("[INFO] WebSocket connected")
#         except Exception as e:
#             print(f"[ERROR] Could not connect WebSocket: {e}")
#             self.ws = None

#     def _connect_signal(self):
#         self.UI.left_sidebar.btn_init_camera.clicked.connect(self._start_camera)
#         self.UI.left_sidebar.btn_stop_camera.clicked.connect(self._stop_camera)
#         print("[INFO] Camera start button connected")

#     def _start_camera(self):
#         self.camera._start_camera()
#         if self.camera.isCamOpen:
#             self.timer.start(30)  # ~30 FPS
#             print("[INFO] Camera started successfully")

#     def _stop_camera(self):
#         if self.camera.cap and self.camera.isCamOpen:
#             self.camera._stop_camera()
#             self.timer.stop()
#             self.UI.center_panel.clear()
#         if self.ws:
#             try:
#                 self.ws.close()
#             except:
#                 pass

#     def _update_frame(self):
#         frame = self.camera._read_frame()
#         if frame is not None:
#             # Display in UI
#             rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             h, w, ch = rgb_frame.shape
#             bytes_per_line = ch * w
#             qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
#             self.UI.center_panel.setPixmap(QPixmap.fromImage(qt_image).scaled(
#                 self.UI.center_panel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
#             ))

#             # Send to server every 15 frames
#             self.frame_counter += 1
#             if self.frame_counter % 15 == 0 and self.ws:
#                 threading.Thread(target=self._send_frame_via_ws, args=(frame,)).start()

#     def _send_frame_via_ws(self, frame):
#         try:
#             success, buffer = cv2.imencode('.png', frame)
#             if success:
#                 self.ws.send(buffer.tobytes(), opcode=websocket.ABNF.OPCODE_BINARY)
#         except Exception as e:
#             print("[ERROR] Failed to send frame via WebSocket:", e)



import cv2
import threading
import websocket
import numpy as np
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QObject
from PyQt5.QtGui import QImage, QPixmap
import time

class WebSocketHandler(QObject):
    image_received = pyqtSignal(np.ndarray)  # emit decoded frame

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.ws_app = None
        self.thread = None

    def start(self):
        self.ws_app = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws_app.on_open = self.on_open
        self.thread = threading.Thread(target=self.ws_app.run_forever, daemon=True)
        self.thread.start()

    def on_message(self, ws, message):
        # WebSocket binary frame → numpy image
        nparr = np.frombuffer(message, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is not None:
            self.image_received.emit(img)

    def on_open(self, ws):
        print("[INFO] WebSocket connected")

    def on_error(self, ws, error):
        print("[ERROR] WebSocket error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("[INFO] WebSocket closed")

    def send(self, data):
        if self.ws_app and self.ws_app.sock and self.ws_app.sock.connected:
            self.ws_app.send(data, opcode=websocket.ABNF.OPCODE_BINARY)

    def close(self):
        if self.ws_app:
            self.ws_app.close()


class ControllerCamera:
    def __init__(self, UI, camera):
        self.UI = UI
        self.camera = camera
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_frame)
        self._connect_signal()
        self.frame_counter = 0
        self.last_sent_frame = None
        self.last_sent = 0
        self.sending = False
        self.ws_handler = WebSocketHandler("ws://localhost:8000/ws/stream/")
        self.ws_handler.image_received.connect(self._display_local_frame)
        self.ws_handler.start()

    def _connect_signal(self):
        self.UI.left_sidebar.btn_init_camera.clicked.connect(self._start_camera)
        self.UI.left_sidebar.btn_stop_camera.clicked.connect(self._stop_camera)
        print("[INFO] Camera start button connected")

    def _start_camera(self):
        self.camera._start_camera()
        if self.camera.isCamOpen:
            self.timer.start(30)
            print("[INFO] Camera started successfully")

    def _stop_camera(self):
        if self.camera.cap and self.camera.isCamOpen:
            self.camera._stop_camera()
            self.timer.stop()
            self.UI.center_panel.clear()
        self.ws_handler.close()



    def _update_frame(self):
        frame = self.camera._read_frame()
        now = time.time()

        # Always show local frame
        self._display_local_frame(frame)

        # Send every 0.5 sec if not already sending
        if now - self.last_sent > 0.5 and not self.sending:
            self.last_sent = now
            self.sending = True
            threading.Thread(target=self._send_frame_via_ws, args=(frame,), daemon=True).start()

    def _send_frame_via_ws(self, frame):
        try:
            success, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
            if success:
                self.ws_handler.send(buffer.tobytes())
        finally:
            self.sending = False

    def _display_local_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.UI.center_panel.setPixmap(QPixmap.fromImage(qt_image).scaled(
            self.UI.center_panel.size(), Qt.KeepAspectRatio, Qt.FastTransformation
        ))


