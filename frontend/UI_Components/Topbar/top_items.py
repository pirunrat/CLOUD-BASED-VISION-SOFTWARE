from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal
from ..Clickable.clickable import ClickableLabel


TOPBAR_ITEM_STYLE = """
QWidget {
    background-color: black;
    color: white;
    border: 1px solid #444;
    border-radius: 4px;
}
QWidget:hover {
    background-color: #333;
    border: 1px solid #888;
}
"""


class TopbarItem(QWidget):
    clicked_signal = pyqtSignal(str)

    def __init__(self, text=None, parent=None):
        super().__init__(parent)
        self.text = text
        self.setMinimumWidth(100)
        self.setMaximumWidth(100)
        self.setStyleSheet(TOPBAR_ITEM_STYLE)
        self.setCursor(Qt.PointingHandCursor)
        self._mainlayout()

    def _mainlayout(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.label = QLabel(f"<div style='text-align:center;'>🖼<br>{self.text}</div>")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white;")
        layout.addWidget(self.label)

    def mousePressEvent(self, event):
        self.clicked_signal.emit(self.text)




        
