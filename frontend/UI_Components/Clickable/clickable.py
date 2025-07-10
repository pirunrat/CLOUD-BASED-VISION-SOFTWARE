from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)
