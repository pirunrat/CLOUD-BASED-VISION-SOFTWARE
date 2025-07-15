from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QAbstractItemView, QHBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPainter, QPixmap


class LEDIndicator(QLabel):
    def __init__(self, color=QColor(0, 255, 0), size=14):
        super().__init__()
        self._color = color
        self._size = size
        self.setFixedSize(size, size)
        self.setPixmap(self._create_pixmap())

    def _create_pixmap(self):
        pixmap = QPixmap(self._size, self._size)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._color)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self._size, self._size)
        painter.end()
        return pixmap


class PLCConnectionPage(QWidget):
    back_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setAutoFillBackground(True)
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: white;
            }

            QLabel#titleLabel {
                font-size: 22px;
                font-weight: bold;
            }

            QTableWidget {
                background-color: #1e1e1e;
                font-size: 16px;
                color: white;
                border-radius: 0px;
                border: 2px solid #444;
                gridline-color: #666; /* Add this for visible cell borders */
            }

            QHeaderView::section {
                background-color: #2d2d2d;
                color: white;
                padding: 10px;
                font-weight: bold;
                border: none;
            }

            QTableWidget::item {
                padding: 8px;
            }
        """)


        # Main layout to fill full black space
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(15)

        # Table that expands full size
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Terminal", "Status"])
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.setShowGrid(True)
        self.table.setAlternatingRowColors(False)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # Populate with example terminals
        terminals = ["Q0.0", "Q0.1", "Q0.2", "Q0.3", "Q0.4"]
        self.table.setRowCount(len(terminals))
        for i, name in enumerate(terminals):
            item = QTableWidgetItem(name)
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(i, 0, item)

            led = LEDIndicator()
            led_container = QWidget()
            led_container.setStyleSheet('background-color: #1e1e1e')
            led_layout = QHBoxLayout()
            led_layout.setContentsMargins(0, 0, 0, 0)
            led_layout.setAlignment(Qt.AlignCenter)
            led_layout.addWidget(led)
            led_container.setLayout(led_layout)

            self.table.setCellWidget(i, 1, led_container)


        # Add table to layout
        main_layout.addWidget(self.table)
