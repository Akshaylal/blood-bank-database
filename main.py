import sys
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui

import bcrypt

from ui_mainwindow import Ui_MainWindow
from ui_login import Ui_LoginDialog

from db import *


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.pushButtonLogin.clicked.connect(self.verify)
        self.pushButtonCancel.clicked.connect(quit)
    
    def verify(self):
        result = session.query(User).filter(User.user == self.inputUsername.text()).first()
        if result == None:
            QMessageBox.warning(self, 'Error', 'Invalid user or password')
            return
        if bcrypt.checkpw(self.inputPassword.text().encode('utf-8'), result.password):
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Invalid user or password')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Shortcut
        #self.quitSc = QShortcut(QKeySequence('Ctrl+Q'), self)
        #self.quitSc.activated.connect(self.quit)
        
        # Menu
        self.actionQuit.triggered.connect(self.quit)
        
        # Find tab
        self.showBloodList()
        self.listBloodFind.currentIndexChanged.connect(self.showBloodList)
        
        # Donate tab
        self.setSearchListDonate()
        self.buttonBoxDonate.accepted.connect(self.saveDonate)
        self.buttonBoxDonate.rejected.connect(self.clearDonate)
        
        # Add Donor tab
        self.buttonBoxAdd.accepted.connect(self.saveAddDonor)
        self.buttonBoxAdd.rejected.connect(self.clearAddDonor)
    
    # Find Blood tab
    def showBloodList(self):
        if self.listBloodFind.currentText() == 'All':
            result = session.query(Donor).join(Blood).all()
        else:
            result = session.query(Donor).join(Blood).filter(Donor.blood_type == self.listBloodFind.currentText()).all()
        if result == None:
            return
        self.tableFind.setRowCount(len(result) + 1)
        self.tableFind.setItem(0,0, QTableWidgetItem('Name'))
        self.tableFind.setItem(0,1, QTableWidgetItem('Phone'))
        self.tableFind.setItem(0,2, QTableWidgetItem('Blood'))
        self.tableFind.setItem(0,3, QTableWidgetItem('Amount'))
        count = 1
        for i in result:
            amount = 0
            for j in i.donate:
                amount += j.amount
            self.tableFind.setItem(count,0, QTableWidgetItem(i.name))
            self.tableFind.setItem(count,1, QTableWidgetItem(str(i.phone)))
            self.tableFind.setItem(count,2, QTableWidgetItem(i.blood_type))
            self.tableFind.setItem(count,3, QTableWidgetItem(str(amount)))
            count += 1
        self.tableFind.horizontalHeader().setStretchLastSection(True) 
        self.tableFind.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        pass
    
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
            QMessageBox.warning(self, 'Error', 'Donor is not registered')
            return
        tmp = Blood(
            amount = self.inputAmountDonate.text(),
            blood_type = self.listBloodDonate.currentText(),
            did = result.did
        )
        session.add(tmp)
        session.commit()
        self.clearDonate()
        self.showBloodList()
        QMessageBox.information(self, 'Success', 'Blood donated')
    
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
        self.showBloodList()
        QMessageBox.information(self, 'Success', 'Donor Added')
    
    def clearAddDonor(self):
        self.inputNameAdd.clear()
        self.inputAgeAdd.clear()
        self.inputSexAdd.clear()
        self.listBloodAdd.setCurrentIndex(-1)
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
    
    login = LoginDialog()
    login.show()
    
    if login.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
