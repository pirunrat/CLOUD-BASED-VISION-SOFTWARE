from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout
import style

class LeftSidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('leftSidebar')
        self.setFixedWidth(300)
        self.setStyleSheet(style.LEFT_SIDEBAR_STYLE)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        cam_label = QLabel("CAMERA")
        cam_label.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)

        self.btn_init_camera = QPushButton("Initialize Camera")
        self.btn_stop_camera = QPushButton("Stop Camera")
        self.btn_load_model = QPushButton("Load Model")
        self.btn_start_detect = QPushButton("Start Detect")

        layout.addWidget(cam_label)
        layout.addWidget(self.btn_init_camera)
        layout.addWidget(self.btn_stop_camera)
        layout.addSpacing(10)

        model_label = QLabel("MODEL")
        model_label.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)

        layout.addWidget(model_label)
        layout.addWidget(self.btn_load_model)
        layout.addWidget(self.btn_start_detect)
        layout.addStretch()
