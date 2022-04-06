from PyQt5.QtWidgets import *
from login_1 import Ui_Form

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = QDialog()
    login_Dialog = Ui_Form()
    login_Dialog.setupUi(main)
    main.show()
    sys.exit(app.exec())