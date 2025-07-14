from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QWidget
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
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)

        # ---- CAMERA Card ----
        camera_card = QFrame()
        camera_card.setStyleSheet(style.CARD_STYLE)
        cam_layout = QVBoxLayout(camera_card)
        cam_layout.setContentsMargins(10, 10, 10, 10)
        cam_layout.setSpacing(10)

        cam_label = QLabel("CAMERA")
        cam_label.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)

        self.btn_init_camera = QPushButton("Initialize Camera")
        self.btn_stop_camera = QPushButton("Stop Camera")

        cam_layout.addWidget(cam_label)
        cam_layout.addWidget(self.btn_init_camera)
        cam_layout.addWidget(self.btn_stop_camera)

        layout.addWidget(camera_card)

        # ---- MODEL Card ----
        model_card = QFrame()
        model_card.setStyleSheet(style.CARD_STYLE)
        model_layout = QVBoxLayout(model_card)
        model_layout.setContentsMargins(10, 10, 10, 10)
        model_layout.setSpacing(10)

        model_label = QLabel("MODEL")
        model_label.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)

        self.btn_load_model = QPushButton("Load Model")
        self.btn_start_detect = QPushButton("Start Detect")

        model_layout.addWidget(model_label)
        model_layout.addWidget(self.btn_load_model)
        model_layout.addWidget(self.btn_start_detect)

        layout.addWidget(model_card)
        layout.addStretch()

