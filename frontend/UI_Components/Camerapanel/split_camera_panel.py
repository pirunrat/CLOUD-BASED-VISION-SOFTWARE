from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt


class SplitCameraPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)

        self.left_camera = QLabel("Camera 1 Feed")
        self.left_camera.setAlignment(Qt.AlignCenter)
        self.left_camera.setStyleSheet("background-color: black; color: white; font-size: 16px; border:1px solid gray")
        self.left_camera.setMaximumWidth(1000)
        self.left_camera.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.right_camera = QLabel("Camera 2 Feed")
        self.right_camera.setAlignment(Qt.AlignCenter)
        self.right_camera.setStyleSheet("background-color: black; color: white; font-size: 16px; border:1px solid gray")
        self.right_camera.setMaximumWidth(1000)
        self.right_camera.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(self.left_camera)
        layout.addWidget(self.right_camera)
