from PyQt5.QtWidgets import (
    QWidget, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QFrame,
    QSizePolicy, QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
import style


class BottomBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('bottombar')
        self.setStyleSheet(style.THUMBNAIL_STYLE)
        self.setMaximumHeight(200)
        self._build_ui()

    def _build_ui(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        container = QWidget()
        container.setStyleSheet(style.THUMBNAIL_STYLE)
        scroll.setWidget(container)

        layout = QHBoxLayout(container)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(20)

        plc_status_card = self._create_plc_status_card()
        plc_output_card = self._create_plc_output_card()

        plc_status_card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        plc_output_card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        layout.addWidget(plc_status_card, 1)  # 20%
        layout.addWidget(plc_output_card, 1)  # 80%

        bar_layout = QVBoxLayout(self)
        bar_layout.setContentsMargins(0, 0, 0, 0)
        bar_layout.addWidget(scroll)

    def _create_plc_status_card(self):
        card = QFrame()
        card.setStyleSheet(style.CARD_STYLE)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        title = QLabel("PLC STATUS")
        title.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)

        self.plc_status_label = QLabel("🟢 Connected")
        self.plc_status_label.setStyleSheet("color: lightgreen; font-size: 14px;")

        self.plc_info_label = QLabel("IP: 192.168.1.10\nPort: 502\nProtocol: Modbus TCP")
        self.plc_info_label.setStyleSheet("color: white; font-size: 12px;")

        layout.addWidget(title)
        layout.addWidget(self.plc_status_label)
        layout.addWidget(self.plc_info_label)

        return card

    def _create_plc_output_card(self):
        card = QFrame()
        card.setStyleSheet(style.CARD_STYLE)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        title = QLabel("PLC OUTPUTS")
        title.setStyleSheet(style.LEFT_SECTION_HEADER_STYLE)
        layout.addWidget(title)

        self.output_table = QTableWidget()
        self.output_table.setColumnCount(2)
        self.output_table.setHorizontalHeaderLabels(["Output", "Status"])
        self.output_table.verticalHeader().setVisible(False)
        self.output_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.output_table.setStyleSheet("""
            QTableWidget {
                background-color: #2c2c2c;
                color: white;
                border: 1px solid #444;
                gridline-color: #555;
            }
            QHeaderView::section {
                background-color: #1e1e1e;
                color: white;
                font-weight: bold;
                padding: 4px;
            }
            QTableWidget::item {
                padding: 6px;
            }
        """)

        plc_outputs = [f"Q0.{i}" for i in range(8)]
        self.output_table.setRowCount(len(plc_outputs))
        self.output_status_cells = []

        for row, output_name in enumerate(plc_outputs):
            output_item = QTableWidgetItem(output_name)
            status_item = QTableWidgetItem("🟢 ON")
            status_item.setForeground(Qt.green)

            self.output_table.setItem(row, 0, output_item)
            self.output_table.setItem(row, 1, status_item)
            self.output_status_cells.append(status_item)

        layout.addWidget(self.output_table)
        return card

    def update_output_status(self, states):
        for item, state in zip(self.output_status_cells, states):
            if state:
                item.setText("🟢 ON")
                item.setForeground(Qt.green)
            else:
                item.setText("🔴 OFF")
                item.setForeground(Qt.red)
