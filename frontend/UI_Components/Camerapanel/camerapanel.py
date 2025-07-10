from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy
import style

class CenterCameraPanel(QLabel):
    def __init__(self, parent=None):
        super().__init__("Camera Feed", parent)
        self.setObjectName('centerPanel')
        self.setStyleSheet(style.MIDDLE_STYLE)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
