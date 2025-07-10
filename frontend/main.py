import sys
from PyQt5.QtWidgets import QApplication
from UI import MainUI # Import MainUI from frontend.UI


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainUI()
    main_window.show()
    sys.exit(app.exec_())


