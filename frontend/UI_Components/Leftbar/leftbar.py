from PyQt5.QtWidgets import (
    QFrame, QLabel, QPushButton, QVBoxLayout, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt
import style  # Assumes style.COMBOBOX_STYLE, style.CARD_STYLE, etc. are defined


class LeftSidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('leftSidebar')
        self.setFixedWidth(200)
        self.setStyleSheet(style.LEFT_SIDEBAR_STYLE)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)

        camera_card = self._create_camera_card()
        model_card = self._create_model_card()

        # Add cards to sidebar
        layout.addWidget(camera_card)
        layout.addWidget(model_card)
        layout.addStretch()

        # Disable camera + detect buttons initially
        self._set_action_buttons_enabled(False)

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

        # Connect model load button
        self.btn_load_model.clicked.connect(self._on_model_loaded)

        layout.addWidget(label)
        layout.addWidget(self.model_selector)
        layout.addWidget(self.btn_load_model)
        layout.addWidget(self.btn_start_detect)

        return card

    def _set_action_buttons_enabled(self, enabled):
        self.btn_init_camera.setEnabled(enabled)
        self.btn_stop_camera.setEnabled(enabled)
        self.btn_start_detect.setEnabled(enabled)

    def _on_model_loaded(self):
        selected_model = self.model_selector.currentText()

        if selected_model == "Select model...":
            QMessageBox.warning(self, "Model Load", "Please select a valid model.")
            return

        # --- Mock model loading logic (replace with real model load) ---
        print(f"Loading model: {selected_model}")
        try:
            # Simulate load
            # model = torch.load(selected_model)
            # model.eval()
            self._set_action_buttons_enabled(True)
            QMessageBox.information(self, "Model Loaded", f"Successfully loaded {selected_model}")
        except Exception as e:
            QMessageBox.critical(self, "Load Failed", f"Failed to load model: {str(e)}")
            self._set_action_buttons_enabled(False)
