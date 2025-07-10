from PyQt5.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import style

class BottomBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('bottombar')
        self.setStyleSheet(style.THUMBNAIL_STYLE)
        self.setMinimumHeight(120)
        self._build_ui()

    def _build_ui(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("border: none;")

        container = QWidget()
        scroll.setWidget(container)

        layout = QHBoxLayout(container)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        for i in range(1, 12):
            thumb = QLabel(f"Image {i}")
            thumb.setFixedSize(100, 80)
            thumb.setAlignment(Qt.AlignCenter)
            thumb.setStyleSheet("""
                background-color: #222;
                border: 2px solid #666;
                border-radius: 6px;
            """)
            layout.addWidget(thumb)

        bar_layout = QVBoxLayout(self)
        bar_layout.setContentsMargins(0, 0, 0, 0)
        bar_layout.addWidget(scroll)
