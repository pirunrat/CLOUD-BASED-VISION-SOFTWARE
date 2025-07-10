from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import cv2
from functools import partial


class ControllerTopbar:
    def __init__(self, topbar_items, main_panel):
        self.main_panel = main_panel

        for item in topbar_items:
            item.clicked_signal.connect(partial(self._on_topbar_click, item.text))

        print("[INFO] Topbar item signal connected")

    def _on_topbar_click(self, key):
        print(f"[INFO] clicked! from {key}")
        self.main_panel.update_right_sidebar(key)



   