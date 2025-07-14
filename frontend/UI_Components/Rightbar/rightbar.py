from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout
import style

class RightSidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('rightSidebar')
        self.setFixedWidth(400)
        self.setStyleSheet(style.RIGHT_SIDEBAR_STYLE)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(18)

        # # --- Login Status ---
        # login_status = QLabel("Logged in as: Admin")
        # login_status.setStyleSheet("font-size: 9pt; color: #bbb; background-color: transparent;")
        # layout.addWidget(login_status)

        # # --- Alert Message ---
        # alert = QLabel("● High scrap rate")
        # alert.setStyleSheet("color: red; font-weight: bold; font-size: 11pt; background-color: transparent;")
        # layout.addWidget(alert)

        # --- Metric Tiles ---
        layout.addWidget(self._make_metric("Total parts inspected", "300", "#ffffff"))
        layout.addWidget(self._make_metric("Inspection rate (parts/min)", "100", "#00eaff"))
        layout.addWidget(self._make_metric("Scrap rate (R)", "8%", "#ff4444"))
        layout.addWidget(self._make_metric("Good parts rate (G)", "92%", "#44ff88"))

        layout.addStretch()

    def _make_metric(self, title, value, color):
        from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame

        container = QFrame()
        container.setStyleSheet(style.METRIC_TILE_STYLE)

        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(8, 4, 8, 4)
        vbox.setSpacing(4)

        label = QLabel(title)
        label.setStyleSheet("font-size: 9pt; color: #aaa; background-color: transparent;")

        number = QLabel(value)
        number.setStyleSheet(f"font-size: 18pt; font-weight: bold; color: {color}; background-color: transparent;")

        vbox.addWidget(label)
        vbox.addWidget(number)

        return container
