import sys
from PySide6.QtWidgets import *
from PySide6 import QtCore

from ui_mainwindow import Ui_MainWindow
from ui_login import Ui_LoginDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionQuit.triggered.connect(self.quit)
    
    def quit(self):
        print("quit")
        quit()
    
    def closeEvent(self, event):
        self.quit()


class Login(QDialog, Ui_LoginDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Login")
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #login = Login()
    #login.show()

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
