from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import cv2
import style

class ControllerCamera:
    def __init__(self, UI, camera):
        self.UI = UI
        self.camera = camera
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_frame)
        self._connect_signal()

    def _connect_signal(self):
        self.UI.left_sidebar.btn_init_camera.clicked.connect(self._start_camera)
        self.UI.left_sidebar.btn_stop_camera.clicked.connect(self._stop_camera)
        print("[INFO] Camera start button connected")

    def _start_camera(self):
        self.camera._start_camera()
        if self.camera.isCamOpen:
            self.timer.start(30)  # ~30 FPS
            print("[INFO] Camera started successfully")
    
    def _stop_camera(self):
        if self.camera.cap and self.camera.isCamOpen:
            self.camera._stop_camera()
            self.UI.center_panel.clear() 
            #self.UI.center_panel.setStyleSheet(style.MIDDLE_STYLE)


    def _update_frame(self):
        frame = self.camera._read_frame()
        if frame is not None:
            # Convert BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.UI.center_panel.setPixmap(QPixmap.fromImage(qt_image).scaled(
                self.UI.center_panel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))
