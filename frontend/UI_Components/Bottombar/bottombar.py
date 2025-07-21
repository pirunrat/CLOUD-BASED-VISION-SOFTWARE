from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class BottomBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('bottombar')
        self.setMinimumHeight(80)
        self.setStyleSheet('background-color: #1e1e1e;')
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        label = QLabel("Deep Visual Insights", self)
        label.setStyleSheet("color: gray; font-size: 16px;")
        layout.addWidget(label)
