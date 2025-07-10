from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QPushButton,
    QScrollArea, QFrame
)
from PyQt5.QtCore import Qt
import style

# ----------------------------- Component Modules -----------------------#
from UI_Components.Bottombar.bottombar import BottomBar
from UI_Components.Camerapanel.camerapanel import CenterCameraPanel
from UI_Components.Leftbar.leftbar import LeftSidebar
from UI_Components.Middlepanel.middlepanel import MiddlePanel
from UI_Components.Rightbar.rightbar import RightSidebar
from UI_Components.Topbar.topbar import TopBar
from UI_Components.Topbar.top_items import TopbarItem
from controller import ControllerCamera

#------------------------------ Camera Module ---------------------------#
from Camera.camera_main import WebCam


class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inspection Dashboard")
        self.setStyleSheet('background-color: white;')
        self.setMinimumSize(1200, 800)
        
       
        
        self._init_topbar_items()
        self._init_middle_panel()
        self._init_topbar()

        self._connect_topbar_signals()
        self._init_layout()

      

    def _init_topbar_items(self):
        self.topbar_item1 = TopbarItem('Item1')
        self.topbar_item2 = TopbarItem('Item2')
        self.topbar_item3 = TopbarItem('Item3')

    def _init_middle_panel(self):
        self.middle_panel = MiddlePanel()
        self.webcam = WebCam()
        self.controller = ControllerCamera(self.middle_panel, self.webcam)

    def _init_topbar(self):
        self.topbar = TopBar(
            [self.topbar_item1, self.topbar_item2, self.topbar_item3],
            self._on_topbar_click
        )
    

    def _connect_topbar_signals(self):
        self.topbar_item1.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item1"))
        self.topbar_item2.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item2"))
        self.topbar_item3.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item3"))

    def _init_layout(self):
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.addWidget(self.topbar)
        self.mainLayout.addWidget(self.middle_panel)
        # Optional: Add bottom bar if needed
        # self.mainLayout.addWidget(self._bottombar())

    def _on_topbar_click(self, key):
        print(f"[INFO] clicked! from {key}")
        self.middle_panel.update_right_sidebar(key)
