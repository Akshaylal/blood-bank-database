# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabFindBlood = QWidget()
        self.tabFindBlood.setObjectName(u"tabFindBlood")
        self.tabWidget.addTab(self.tabFindBlood, "")
        self.tabDonate = QWidget()
        self.tabDonate.setObjectName(u"tabDonate")
        self.tabWidget.addTab(self.tabDonate, "")
        self.tabAddDonor = QWidget()
        self.tabAddDonor.setObjectName(u"tabAddDonor")
        self.gridLayout_2 = QGridLayout(self.tabAddDonor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(6)
        self.label = QLabel(self.tabAddDonor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.inputNameAdd = QLineEdit(self.tabAddDonor)
        self.inputNameAdd.setObjectName(u"inputNameAdd")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputNameAdd)

        self.label_2 = QLabel(self.tabAddDonor)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.inputAgeAdd = QLineEdit(self.tabAddDonor)
        self.inputAgeAdd.setObjectName(u"inputAgeAdd")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputAgeAdd)

        self.label_3 = QLabel(self.tabAddDonor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.inputSexAdd = QLineEdit(self.tabAddDonor)
        self.inputSexAdd.setObjectName(u"inputSexAdd")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputSexAdd)

        self.label_4 = QLabel(self.tabAddDonor)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.inputPhoneAdd = QLineEdit(self.tabAddDonor)
        self.inputPhoneAdd.setObjectName(u"inputPhoneAdd")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputPhoneAdd)

        self.label_5 = QLabel(self.tabAddDonor)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.inputAddressAdd = QPlainTextEdit(self.tabAddDonor)
        self.inputAddressAdd.setObjectName(u"inputAddressAdd")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.inputAddressAdd)

        self.label_6 = QLabel(self.tabAddDonor)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_6)

        self.buttonBoxAdd = QDialogButtonBox(self.tabAddDonor)
        self.buttonBoxAdd.setObjectName(u"buttonBoxAdd")
        self.buttonBoxAdd.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.buttonBoxAdd)


        self.gridLayout_2.addLayout(self.formLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tabAddDonor, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Blood Bank Database", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFindBlood), QCoreApplication.translate("MainWindow", u"Find Blood", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDonate), QCoreApplication.translate("MainWindow", u"Donate Blood", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Age :", None))
        self.inputAgeAdd.setInputMask(QCoreApplication.translate("MainWindow", u"99", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sex :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Phone :", None))
        self.inputPhoneAdd.setInputMask(QCoreApplication.translate("MainWindow", u"9999999999", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.label_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAddDonor), QCoreApplication.translate("MainWindow", u"Add Donor", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

