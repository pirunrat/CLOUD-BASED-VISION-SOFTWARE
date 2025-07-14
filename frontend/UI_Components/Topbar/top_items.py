from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from ..Clickable.clickable import ClickableLabel
import style

# TOPBAR_ITEM_STYLE = """
# QWidget {
#     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0,
#                 stop:0 #2c2c2c, stop:1 #555555);;
#     color: white;
#     border: 1px solid lightgray;
#     border-radius: 0px;
# }
# QWidget:hover {
#     background-color: #222;
# }
# """

class TopbarItem(QWidget):
    clicked_signal = pyqtSignal(str)

    def __init__(self, text=None, image=None, parent=None):
        super().__init__(parent)
        self.text = text
        self.image = image  # File path 
        self.parent = parent
        self.setMinimumHeight(100)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(style.TOPBAR_ITEM_STYLE)
        self.setCursor(Qt.PointingHandCursor)
        self._mainlayout()

    def _mainlayout(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # HTML label with image and text
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextFormat(Qt.RichText)

        # Format image as base64 or use file path directly
        if isinstance(self.image, str):
            self.label.setText(f"""
                <div style='text-align:center;'>
                    <img src='{self.image}' width='48' height='48'><br>
                    <span style='color:white;font-size:10pt;'>{self.text}</span>
                </div>
            """)
        else:
            self.label.setText(f"""
                <div style='text-align:center;'>
                    🖼<br><span style='color:white;font-size:10pt;'>{self.text}</span>
                </div>
            """)

        layout.addWidget(self.label)

    def mousePressEvent(self, event):
        self.clicked_signal.emit(self.text)
