from PyQt5.QtWidgets import QLabel,QSizePolicy,QHBoxLayout
from PyQt5.QtCore import Qt
import style



class TopBar(QLabel):
    def __init__(self, items,on_item_clicked ,parent=None):
        super().__init__("", parent)
        self.setObjectName('topbar')
        self.setMinimumHeight(100)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setStyleSheet(style.TOPBAR_STYLE)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMargin(0)



        self._mainlayout(items, on_item_clicked)

    def _mainlayout(self, items, on_item_clicked):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft)
        self.setLayout(layout)

        # ✅ Add shared instances to layout
        for item in items:
            layout.addWidget(item)
            item.clicked_signal.connect(on_item_clicked)



