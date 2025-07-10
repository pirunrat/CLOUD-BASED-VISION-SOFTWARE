# TOPBAR_STYLE = """
# QLabel#topbar {
#     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
#                                       stop:0 #3a3a3a, stop:1 #707070);
#     color: white;
#     padding: 10px;
#     font-size: 16pt;
# }
# """

# BOTTOMBAR_STYLE = """
# QLabel#bottombar {
#     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
#                                       stop:0 #3a3a3a, stop:1 #707070);
#     color: white;
#     padding: 10px;
#     font-size: 14pt;
# }
# """

# LEFT_SIDEBAR_STYLE = """
# QWidget#leftSidebar {
#     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
#                                       stop:0 #2c2c2c, stop:1 #555555);
#     color: white;
#     padding: 10px;
# }
# """

# RIGHT_SIDEBAR_STYLE = """
# QWidget#rightSidebar {
#     background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0,
#                                       stop:0 #2c2c2c, stop:1 #555555);
#     color: white;
#     padding: 20px;
#     border-left: 1px solid #888;
#     font-family: 'Segoe UI', sans-serif;
# }
# QLabel {
#     font-size: 10pt;
#     color: #ddd;
# }
# """


# MIDDLE_STYLE = """
# QLabel#centerPanel {
#     background-color: black;
#     color: #333;
#     font-size: 14pt;
#     border-left: 1px solid #ccc;
#     border-right: 1px solid #ccc;
# }
# """

# BUTTON_STYLE = """
# QPushButton {
#     background-color: #444;
#     color: white;
#     border: 1px solid #666;
#     border-radius: 6px;
#     padding: 6px;
#     font-size: 10pt;
# }
# QPushButton:hover {
#     background-color: #555;
# }
# QPushButton:pressed {
#     background-color: #333;
# }
# """


# # Right Sidebar Metric Box
# METRIC_TILE_STYLE = """
# QWidget {
#     background-color: rgba(255, 255, 255, 0.05);
#     border-radius: 10px;
#     padding: 10px;
#     margin-bottom: 6px;
# }
# QLabel {
#     color: #ddd;
#     font-family: 'Segoe UI', sans-serif;
# }
# """

# # Better Left Sidebar Section Headers
# LEFT_SECTION_HEADER_STYLE = """
# font-weight: bold;
# font-size: 12pt;
# color: white;
# margin-bottom: 6px;
# """

# # Left Sidebar Buttons
# BUTTON_STYLE = """
# QPushButton {
#     background-color: #3c3c3c;
#     color: white;
#     border: 1px solid #666;
#     border-radius: 8px;
#     padding: 8px;
#     font-size: 10pt;
# }
# QPushButton:hover {
#     background-color: #505050;
# }
# QPushButton:pressed {
#     background-color: #2a2a2a;
# }
# """



TOPBAR_STYLE = """
QLabel#topbar {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
                                      stop:0 #3a3a3a, stop:1 #707070);
    color: white;
    padding: 10px;
    font-size: 16pt;
}
"""

BOTTOMBAR_STYLE = """
QWidget#bottombar {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                      stop:0 #3a3a3a, stop:1 #707070);
    padding: 5px;
}
QLabel {
    color: white;
    font-size: 12pt;
}
"""

LEFT_SIDEBAR_STYLE = """
QFrame#leftSidebar {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                      stop:0 #2c2c2c, stop:1 #555555);
    padding: 10px;
}

QFrame#leftSidebar QLabel {
    color: white;
    background-color: transparent;
    font-weight: bold;
}

QFrame#leftSidebar QPushButton {
    background-color: #444;
    color: white;
    border: 1px solid #666;
    border-radius: 6px;
    padding: 6px;
    font-size: 10pt;
}
QFrame#leftSidebar QPushButton:hover {
    background-color: #555;
}
QFrame#leftSidebar QPushButton:pressed {
    background-color: #2a2a2a;
}
"""




RIGHT_SIDEBAR_STYLE = """
QFrame#rightSidebar {
    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0,
                                      stop:0 #2c2c2c, stop:1 #555555);
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

LEFT_SECTION_HEADER_STYLE = """
font-weight: bold;
font-size: 12pt;
color: white;
margin-bottom: 6px;
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
QWidget#bottombar {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                      stop:0 #3a3a3a, stop:1 #707070);
}
QLabel {
    color: white;
    font-size: 10pt;
}
"""
