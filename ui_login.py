# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(400, 300)
        LoginDialog.setMinimumSize(QSize(400, 300))
        LoginDialog.setMaximumSize(QSize(400, 300))
        self.gridLayout = QGridLayout(LoginDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(LoginDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.inputUsername = QLineEdit(LoginDialog)
        self.inputUsername.setObjectName(u"inputUsername")

        self.gridLayout.addWidget(self.inputUsername, 0, 1, 1, 2)

        self.label_2 = QLabel(LoginDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.inputPassword = QLineEdit(LoginDialog)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.inputPassword, 1, 1, 1, 2)

        self.pushButtonLogin = QPushButton(LoginDialog)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")

        self.gridLayout.addWidget(self.pushButtonLogin, 2, 1, 1, 1)

        self.pushButtonCancel = QPushButton(LoginDialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.gridLayout.addWidget(self.pushButtonCancel, 2, 2, 1, 1)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginDialog", u"Username :", None))
        self.label_2.setText(QCoreApplication.translate("LoginDialog", u"Password :", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("LoginDialog", u"Cancel", None))
    # retranslateUi

