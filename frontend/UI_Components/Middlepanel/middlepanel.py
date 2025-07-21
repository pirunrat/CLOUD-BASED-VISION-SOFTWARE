from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy
from ..Leftbar.leftbar import LeftSidebar
from ..Camerapanel.split_camera_panel import SplitCameraPanel  # ✅ New import
from ..Rightbar.rightbar import RightSidebar
from ..Rightbar.rightbar_2 import RightSidebar2
import style


class MiddlePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(style.MIDDLE_STYLE)

        # -- UI Components
        self.left_sidebar = LeftSidebar()
        self.center_panel = SplitCameraPanel()  # ✅ Changed to SplitCameraPanel
        self.center_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Rightbar container (acts like a stack manually)
        self.rightbar_container = QWidget()
        self.rightbar_layout = QVBoxLayout(self.rightbar_container)
        self.rightbar_layout.setContentsMargins(0, 0, 0, 0)
        self.rightbar_layout.setSpacing(0)

        self.rightbars = {
            # Optional: Add named sidebars here later
        }

        for key, widget in self.rightbars.items():
            self.rightbar_layout.addWidget(widget)
            widget.hide()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.main_content_layout = QHBoxLayout()
        self.main_content_layout.setContentsMargins(0, 0, 0, 0)
        self.main_content_layout.setSpacing(0)

        self.main_content_layout.addWidget(self.left_sidebar)
        self.main_content_layout.addWidget(self.center_panel)
        # self.main_content_layout.addWidget(self.rightbar_container)

        layout.addLayout(self.main_content_layout)

    def update_right_sidebar(self, key):
        print(f"[DEBUG] update_right_sidebar: {key}")
        if key in self.rightbars:
            self.current_rightbar.hide()
            self.current_rightbar = self.rightbars[key]
            self.current_rightbar.show()
