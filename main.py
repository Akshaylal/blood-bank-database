import sys
from PySide6.QtWidgets import *
from PySide6 import QtCore
#from PySide6.QtGui import QShortcut, QKeySequence

from ui_mainwindow import Ui_MainWindow

from db import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Shortcut
        #self.quitSc = QShortcut(QKeySequence('Ctrl+Q'), self)
        #self.quitSc.activated.connect(self.quit)
        
        # Menu
        self.actionQuit.triggered.connect(self.quit)
        
        # Donate tab
        self.setSearchListDonate()
        self.buttonBoxDonate.accepted.connect(self.saveDonate)
        self.buttonBoxDonate.rejected.connect(self.clearDonate)
        
        # Add Donor tab
        self.buttonBoxAdd.accepted.connect(self.saveAddDonor)
        self.buttonBoxAdd.rejected.connect(self.clearAddDonor)
    
    # Find Blood tab
    
    # Donate Blood tab
    def setSearchListDonate(self):
        result = session.query(Donor).all()
        r = []
        for i in result:
            r.append(i.name)
        completer = QCompleter(r, self)
        self.inputNameDonate.setCompleter(completer)
    
    def saveDonate(self):
        result = session.query(Donor).filter(Donor.name == self.inputNameDonate.text()).first()
        if result == None:
            print('Donor does not exist')
            return
        tmp = Blood(
            amount = self.inputAmountDonate.text(),
            blood_type = self.listBloodDonate.currentText(),
            did = result.did
        )
        session.add(tmp)
        session.commit()
        self.clearDonate()
        print('save')
    
    def clearDonate(self):
        self.inputNameDonate.clear()
        self.listBloodDonate.setCurrentIndex(-1)
        self.inputAmountDonate.clear()
    
    # Add Donor tab
    def saveAddDonor(self):
        tmp = Donor(
            name = self.inputNameAdd.text(),
            sex = self.inputSexAdd.text(),
            age = self.inputAgeAdd.text(),
            blood_type = self.listBloodAdd.currentText(),
            address = self.inputAddressAdd.toPlainText(),
            phone = self.inputPhoneAdd.text()
        )
        session.add(tmp)
        session.commit()
        self.clearAddDonor()
        self.setSearchListDonate()
    
    def clearAddDonor(self):
        self.inputNameAdd.clear()
        self.inputAgeAdd.clear()
        self.inputSexAdd.clear()
        self.inputPhoneAdd.clear()
        self.inputAddressAdd.clear()
    
    # Quit
    def quit(self):
        print('quit')
        quit()
    
    def closeEvent(self, event):
        self.quit()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
