# from PyQt5.QtWidgets import (
#     QWidget, QVBoxLayout
# )
# from PyQt5.QtCore import Qt

# # ----------------------------- Component Modules -----------------------#
# from UI_Components.Bottombar.bottombar import BottomBar
# from UI_Components.Camerapanel.camerapanel import CenterCameraPanel
# from UI_Components.Leftbar.leftbar import LeftSidebar
# from UI_Components.Middlepanel.middlepanel import MiddlePanel
# from UI_Components.Rightbar.rightbar import RightSidebar
# from UI_Components.Topbar.topbar import TopBar
# from UI_Components.Topbar.top_items import TopbarItem
# from UI_Components.PLCConnection.plc_connection_page import PLCConnectionPage
# from controller import ControllerCamera

# #------------------------------ Camera Module ---------------------------#
# from Camera.camera_main import WebCam


# class MainUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Inspection Dashboard")
#         self.setMinimumSize(1200, 800)

#         self.current_main_widget = None

#         self._init_topbar_items()
#         self._init_middle_panel()
#         self._init_topbar()
#         self._init_bottombar()
#         self._connect_topbar_signals()
#         self._init_layout()

#     def _init_topbar_items(self):
#         self.topbar_item1 = TopbarItem('DEEP LEARNING', image=r"assets/deep-learning.png")
#         self.topbar_item2 = TopbarItem('MATCHING', image=r"assets/test-match.png")
#         self.topbar_item3 = TopbarItem('MEASUREMENT', image=r"assets/ruler.png")
#         self.topbar_item4 = TopbarItem('PLC CONNECTION', image=r"assets/plc.png")

#     def _init_middle_panel(self):
#         self.middle_panel = MiddlePanel()
#         self.webcam = WebCam()
#         self.controller = ControllerCamera(self.middle_panel, self.webcam)

#     def _init_topbar(self):
#         self.topbar = TopBar(
#             [self.topbar_item1, self.topbar_item2, self.topbar_item3, self.topbar_item4],
#             self._on_topbar_click
#         )

#     def _init_bottombar(self):
#         self.bottombar = BottomBar()

#     def _connect_topbar_signals(self):
#         self.topbar_item1.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item1"))
#         self.topbar_item2.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item2"))
#         self.topbar_item3.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item3"))

#     # def _init_layout(self):
#     #     self.mainLayout = QVBoxLayout(self)
#     #     self.mainLayout.setContentsMargins(0, 0, 0, 0)
#     #     self.mainLayout.setSpacing(0)

#     #     self.mainLayout.addWidget(self.topbar)

#     #     # 🔧 Create a container QWidget to hold dynamic content
#     #     self.content_widget = QWidget()
#     #     self.content_layout = QVBoxLayout(self.content_widget)
#     #     self.content_layout.setContentsMargins(0, 0, 0, 0)
#     #     self.content_layout.setSpacing(0)

#     #     self.mainLayout.addWidget(self.content_widget)
#     #     self.mainLayout.addWidget(self.bottombar)

#     #     self._set_main_content(self.middle_panel)

#     def _init_layout(self):
#         # Create a top-level container to manage margins properly
#         self.container_widget = QWidget()
#         self.mainLayout = QVBoxLayout()
#         self.mainLayout.setContentsMargins(0, 0, 0, 0)
#         self.mainLayout.setSpacing(0)

#         self.mainLayout.addWidget(self.topbar)

#         # Dynamic content area
#         self.content_widget = QWidget()
#         self.content_layout = QVBoxLayout(self.content_widget)
#         self.content_layout.setContentsMargins(0, 0, 0, 0)
#         self.content_layout.setSpacing(0)
#         self.mainLayout.addWidget(self.content_widget)

#         # Bottombar
#         self.mainLayout.addWidget(self.bottombar)

#         # Apply layout to container, then set that container as central
#         self.container_widget.setLayout(self.mainLayout)

#         # Set the final layout for MainUI
#         outer_layout = QVBoxLayout()
#         outer_layout.setContentsMargins(0, 0, 0, 0)
#         outer_layout.setSpacing(0)
#         outer_layout.addWidget(self.container_widget)
#         self.setLayout(outer_layout)

#         self._set_main_content(self.middle_panel)


#     def _set_main_content(self, widget):
#         if self.current_main_widget:
#             self.content_layout.removeWidget(self.current_main_widget)
#             self.current_main_widget.setParent(None)

#         self.content_layout.addWidget(widget)
#         self.current_main_widget = widget


#     def _on_topbar_click(self, key):
#         print(f"[INFO] clicked! from {key}")
#         if key == "PLC CONNECTION":
#             plc_page = PLCConnectionPage()
#             plc_page.back_signal.connect(lambda: self._set_main_content(self.middle_panel))
#             self._set_main_content(plc_page)
#         else:
#             self._set_main_content(self.middle_panel)
#             self.middle_panel.update_right_sidebar(key)



from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt

# ----------------------------- Component Modules -----------------------#
from UI_Components.Bottombar.bottombar import BottomBar
from UI_Components.Camerapanel.camerapanel import CenterCameraPanel
from UI_Components.Leftbar.leftbar import LeftSidebar
from UI_Components.Middlepanel.middlepanel import MiddlePanel
from UI_Components.Rightbar.rightbar import RightSidebar
from UI_Components.Topbar.topbar import TopBar
from UI_Components.Topbar.top_items import TopbarItem
from UI_Components.PLCConnection.plc_connection_page import PLCConnectionPage
from controller import ControllerCamera

# ------------------------------ Camera Module ---------------------------#
from Camera.camera_main import WebCam


class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inspection Dashboard")
        self.setStyleSheet('background-color:black')
        self.setMinimumSize(1200, 800)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.current_main_widget = None

        self._init_topbar_items()
        self._init_middle_panel()
        self._init_topbar()
        self._init_bottombar()
        self._connect_topbar_signals()
        self._init_layout()

    def _init_topbar_items(self):
        self.topbar_item1 = TopbarItem('DEEP LEARNING', image=r"assets/deep-learning.png")
        self.topbar_item2 = TopbarItem('MATCHING', image=r"assets/test-match.png")
        self.topbar_item3 = TopbarItem('MEASUREMENT', image=r"assets/ruler.png")
        self.topbar_item4 = TopbarItem('PLC CONNECTION', image=r"assets/plc.png")

    def _init_middle_panel(self):
        self.middle_panel = MiddlePanel()
        self.webcam = WebCam()
        self.controller = ControllerCamera(self.middle_panel, self.webcam)

    def _init_topbar(self):
        self.topbar = TopBar(
            [self.topbar_item1, self.topbar_item2, self.topbar_item3, self.topbar_item4],
            self._on_topbar_click
        )
        self.topbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def _init_bottombar(self):
        self.bottombar = BottomBar()
        self.bottombar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def _connect_topbar_signals(self):
        self.topbar_item1.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item1"))
        self.topbar_item2.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item2"))
        self.topbar_item3.clicked_signal.connect(lambda: self.middle_panel.update_right_sidebar("Item3"))

    def _init_layout(self):
        # Top-level container widget
        self.container_widget = QWidget()
        self.mainLayout = QVBoxLayout(self.container_widget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.mainLayout.addWidget(self.topbar)

        # Dynamic content widget container
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        self.mainLayout.addWidget(self.content_widget)

        self.mainLayout.addWidget(self.bottombar)

        # Final layout for MainUI
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)
        outer_layout.addWidget(self.container_widget)

        self.setLayout(outer_layout)
        self._set_main_content(self.middle_panel)

    def _set_main_content(self, widget):
        if self.current_main_widget:
            self.content_layout.removeWidget(self.current_main_widget)
            self.current_main_widget.setParent(None)

        self.content_layout.addWidget(widget)
        self.current_main_widget = widget

    def _on_topbar_click(self, key):
        print(f"[INFO] clicked! from {key}")
        if key == "PLC CONNECTION":
            plc_page = PLCConnectionPage()
            plc_page.back_signal.connect(lambda: self._set_main_content(self.middle_panel))
            self._set_main_content(plc_page)
        else:
            self._set_main_content(self.middle_panel)
            self.middle_panel.update_right_sidebar(key)
