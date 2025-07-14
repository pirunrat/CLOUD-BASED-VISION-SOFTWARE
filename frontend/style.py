COMBOBOX_STYLE = """
QComboBox {
    padding: 6px;
    font-size: 14px;
    border: 1px solid #888;
    border-radius: 5px;
    background-color: #2b2b2b;
    color: white;
}
QComboBox QAbstractItemView {
    background-color: #2e2e2e;
    selection-background-color: #555555;
    color: white;
}
"""




TOPBAR_ITEM_STYLE = """
QWidget {
    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,
                stop:0 #1a1a1a, stop:1 #3a3a3a);
    color: white;
    border: 1px solid black;
    border-radius: 0px;
}
QWidget:hover {
    background-color: #222;
}
"""




TOPBAR_STYLE = """
QLabel#topbar {
    background-color: qqlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,
                stop:0 #1a1a1a, stop:1 #3a3a3a);
    color: white;
    padding: 10px;
    font-size: 16pt;
}
"""

BOTTOMBAR_STYLE = """
QWidget#bottombar {
    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,
                stop:0 #1a1a1a, stop:1 #3a3a3a);
    padding: 5px;
}
QLabel {
    color: white;
    font-size: 12pt;
}
"""






RIGHT_SIDEBAR_STYLE = """
QFrame#rightSidebar {
    background-color: #1e1e1e;

    padding: 20px;
    border-left: 1px solid #444;
}

QFrame#rightSidebar QLabel {
    color: #ddd;
    background-color: transparent;
}
"""



MIDDLE_STYLE = """
QLabel#centerPanel {
    background-color: black;
    color: #333;
    font-size: 14pt;
    border-left: 1px solid #ccc;
    border-right: 1px solid #ccc;
}
"""

BUTTON_STYLE = """
QPushButton {
    background-color: #444;
    color: white;
    border: 1px solid #666;
    border-radius: 8px;
    padding: 8px;
    font-size: 10pt;
}
QPushButton:hover {
    background-color: #555;
}
QPushButton:pressed {
    background-color: #2a2a2a;
}
"""

CARD_STYLE = """
QFrame {
    background-color: #1e1e1e;
    border-radius: 10px;
    border: 1px solid #333;
}
"""

CARD_STYLE = """
QFrame {
    background-color: #2e2e2e;
    border-radius: 10px;
    border: 1px solid #444;
}
"""

LEFT_SECTION_HEADER_STYLE = """
QLabel {
    font-size: 16px;
    font-weight: bold;
    color: white;
}
"""


LEFT_SIDEBAR_STYLE = """
QFrame#leftSidebar {
    background-color: #1e1e1e;
}
QPushButton {
    background-color: #333;
    color: white;
    padding: 6px 12px;
    border: 1px solid #444;
    border-radius: 6px;
}
QPushButton:hover {
    background-color: #444;
}
"""


METRIC_TILE_STYLE = """
QWidget {
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    padding: 10px;
}
QLabel {
    color: #ddd;
}
"""

THUMBNAIL_STYLE = """
QWidget {
    background-color:  #1e1e1e;
    border: 1px solid black;
}
QLabel {
    background-color:   #1e1e1e;
    font-size: 10pt;
}
"""
