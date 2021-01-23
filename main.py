import sys
from PySide6.QtWidgets import *
from PySide6 import QtCore

from ui_mainwindow import Ui_MainWindow

from db import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        #Quit
        self.actionQuit.triggered.connect(self.quit)
        
        # Add Donor tab
        self.buttonBoxAdd.accepted.connect(self.saveAddDonor)
        self.buttonBoxAdd.rejected.connect(self.clearAddDonor)
    
    # Find Blood tab
    
    # Donate Blood tab
    
    # Add Donor tab
    def saveAddDonor(self):
        tmp = Donor(
            name = self.inputNameAdd.text(),
            sex = self.inputSexAdd.text(),
            age = self.inputAgeAdd.text(),
            address = self.inputAddressAdd.toPlainText(),
            phone = self.inputPhoneAdd.text()
        )
        session.add(tmp)
        session.commit()
        self.clearAddDonor()
    
    def clearAddDonor(self):
        self.inputNameAdd.clear()
        self.inputAgeAdd.clear()
        self.inputSexAdd.clear()
        self.inputPhoneAdd.clear()
        self.inputAddressAdd.clear()
    
    # Quit
    def quit(self):
        print("quit")
        quit()
    
    def closeEvent(self, event):
        self.quit()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
