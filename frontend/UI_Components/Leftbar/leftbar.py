from PyQt5.QtWidgets import (
    QFrame, QLabel, QPushButton, QVBoxLayout, QComboBox
)
import style  # style.COMBOBOX_STYLE and others assumed defined

class LeftSidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('leftSidebar')
        self.setFixedWidth(400)
        self.setStyleSheet(style.LEFT_SIDEBAR_STYLE)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)

        camera_card = self._create_camera_card()
        model_card = self._create_model_card()

        layout.addWidget(camera_card)
        layout.addWidget(model_card)
        layout.addStretch()

    def _create_camera_card(self):
        card = QFrame()
        card.setStyleSheet(style.CARD_STYLE)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        label = QLabel("CAMERA")
        label.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)

        self.btn_init_camera = QPushButton("Initialize Camera")
        self.btn_stop_camera = QPushButton("Stop Camera")

        layout.addWidget(label)
        layout.addWidget(self.btn_init_camera)
        layout.addWidget(self.btn_stop_camera)

        return card

    def _create_model_card(self):
        card = QFrame()
        card.setStyleSheet(style.CARD_STYLE)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        label = QLabel("MODEL")
        label.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)

        self.model_selector = QComboBox()
        self.model_selector.setStyleSheet(style.COMBOBOX_STYLE)
        self.model_selector.addItems([
            "Select model...",
            "defect_model_v1.pt",
            "defect_model_v2.pt",
            "classifier_x.pt"
        ])

        self.btn_load_model = QPushButton("Load Model")
        self.btn_start_detect = QPushButton("Start Detect")

        layout.addWidget(label)
        layout.addWidget(self.model_selector)
        layout.addWidget(self.btn_load_model)
        layout.addWidget(self.btn_start_detect)

        return card
