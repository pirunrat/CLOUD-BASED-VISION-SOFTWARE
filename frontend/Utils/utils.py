import os
from PyQt5.QtWidgets import (
    QSlider, QLineEdit, QPushButton, QCheckBox,
    QComboBox, QSpinBox, QSlider, QSizePolicy
)
from PyQt5.QtCore import Qt





def slider(min_val=0, max_val=255, init_val=128):
    s = QSlider(Qt.Horizontal)
    s.setRange(min_val, max_val)
    s.setValue(init_val)
    s.setFixedHeight(20)  # ✅ Prevents vertical squeezing
    s.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return s


def text_input(placeholder: str = "Enter text") -> QLineEdit:
    line = QLineEdit()
    line.setPlaceholderText(placeholder)
    return line


def button(text: str = "Click Me", enabled: bool = True) -> QPushButton:
    btn = QPushButton(text)
    btn.setEnabled(enabled)
    return btn



def checkbox(text: str = "Check me") -> QCheckBox:
    cb = QCheckBox(text)
    return cb


def combo_box(items: list[str] = ["Option 1", "Option 2"]) -> QComboBox:
    combo = QComboBox()
    combo.addItems(items)
    return combo


def spin_box(min_val=0, max_val=100, init_val=0) -> QSpinBox:
    spin = QSpinBox()
    spin.setRange(min_val, max_val)
    spin.setValue(init_val)
    return spin