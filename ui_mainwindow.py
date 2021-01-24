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
        icon = QIcon()
        iconThemeName = u"exit.png"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.actionQuit.setIcon(icon)
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
        self.gridLayout_3 = QGridLayout(self.tabDonate)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formDonate = QFormLayout()
        self.formDonate.setObjectName(u"formDonate")
        self.formDonate.setHorizontalSpacing(20)
        self.label_7 = QLabel(self.tabDonate)
        self.label_7.setObjectName(u"label_7")

        self.formDonate.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.inputNameDonate = QLineEdit(self.tabDonate)
        self.inputNameDonate.setObjectName(u"inputNameDonate")

        self.formDonate.setWidget(0, QFormLayout.FieldRole, self.inputNameDonate)

        self.label_8 = QLabel(self.tabDonate)
        self.label_8.setObjectName(u"label_8")

        self.formDonate.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.listBloodDonate = QComboBox(self.tabDonate)
        self.listBloodDonate.addItem("")
        self.listBloodDonate.addItem("")
        self.listBloodDonate.addItem("")
        self.listBloodDonate.addItem("")
        self.listBloodDonate.addItem("")
        self.listBloodDonate.addItem("")
        self.listBloodDonate.addItem("")
        self.listBloodDonate.addItem("")
        self.listBloodDonate.setObjectName(u"listBloodDonate")

        self.formDonate.setWidget(1, QFormLayout.FieldRole, self.listBloodDonate)

        self.label_10 = QLabel(self.tabDonate)
        self.label_10.setObjectName(u"label_10")

        self.formDonate.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.inputAmountDonate = QLineEdit(self.tabDonate)
        self.inputAmountDonate.setObjectName(u"inputAmountDonate")

        self.formDonate.setWidget(2, QFormLayout.FieldRole, self.inputAmountDonate)

        self.buttonBox = QDialogButtonBox(self.tabDonate)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formDonate.setWidget(4, QFormLayout.FieldRole, self.buttonBox)

        self.label_11 = QLabel(self.tabDonate)
        self.label_11.setObjectName(u"label_11")

        self.formDonate.setWidget(3, QFormLayout.FieldRole, self.label_11)


        self.gridLayout_3.addLayout(self.formDonate, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tabDonate, "")
        self.tabAddDonor = QWidget()
        self.tabAddDonor.setObjectName(u"tabAddDonor")
        self.gridLayout_2 = QGridLayout(self.tabAddDonor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formAdd = QFormLayout()
        self.formAdd.setObjectName(u"formAdd")
        self.formAdd.setHorizontalSpacing(20)
        self.formAdd.setVerticalSpacing(6)
        self.label = QLabel(self.tabAddDonor)
        self.label.setObjectName(u"label")

        self.formAdd.setWidget(0, QFormLayout.LabelRole, self.label)

        self.inputNameAdd = QLineEdit(self.tabAddDonor)
        self.inputNameAdd.setObjectName(u"inputNameAdd")

        self.formAdd.setWidget(0, QFormLayout.FieldRole, self.inputNameAdd)

        self.label_2 = QLabel(self.tabAddDonor)
        self.label_2.setObjectName(u"label_2")

        self.formAdd.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.inputAgeAdd = QLineEdit(self.tabAddDonor)
        self.inputAgeAdd.setObjectName(u"inputAgeAdd")

        self.formAdd.setWidget(1, QFormLayout.FieldRole, self.inputAgeAdd)

        self.label_3 = QLabel(self.tabAddDonor)
        self.label_3.setObjectName(u"label_3")

        self.formAdd.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.inputSexAdd = QLineEdit(self.tabAddDonor)
        self.inputSexAdd.setObjectName(u"inputSexAdd")

        self.formAdd.setWidget(2, QFormLayout.FieldRole, self.inputSexAdd)

        self.label_4 = QLabel(self.tabAddDonor)
        self.label_4.setObjectName(u"label_4")

        self.formAdd.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.inputPhoneAdd = QLineEdit(self.tabAddDonor)
        self.inputPhoneAdd.setObjectName(u"inputPhoneAdd")

        self.formAdd.setWidget(4, QFormLayout.FieldRole, self.inputPhoneAdd)

        self.label_5 = QLabel(self.tabAddDonor)
        self.label_5.setObjectName(u"label_5")

        self.formAdd.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.inputAddressAdd = QPlainTextEdit(self.tabAddDonor)
        self.inputAddressAdd.setObjectName(u"inputAddressAdd")

        self.formAdd.setWidget(5, QFormLayout.FieldRole, self.inputAddressAdd)

        self.label_6 = QLabel(self.tabAddDonor)
        self.label_6.setObjectName(u"label_6")

        self.formAdd.setWidget(6, QFormLayout.FieldRole, self.label_6)

        self.buttonBoxAdd = QDialogButtonBox(self.tabAddDonor)
        self.buttonBoxAdd.setObjectName(u"buttonBoxAdd")
        self.buttonBoxAdd.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.formAdd.setWidget(7, QFormLayout.FieldRole, self.buttonBoxAdd)

        self.label_9 = QLabel(self.tabAddDonor)
        self.label_9.setObjectName(u"label_9")

        self.formAdd.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.listBloodAdd = QComboBox(self.tabAddDonor)
        self.listBloodAdd.addItem("")
        self.listBloodAdd.addItem("")
        self.listBloodAdd.addItem("")
        self.listBloodAdd.addItem("")
        self.listBloodAdd.addItem("")
        self.listBloodAdd.addItem("")
        self.listBloodAdd.addItem("")
        self.listBloodAdd.addItem("")
        self.listBloodAdd.setObjectName(u"listBloodAdd")

        self.formAdd.setWidget(3, QFormLayout.FieldRole, self.listBloodAdd)


        self.gridLayout_2.addLayout(self.formAdd, 1, 1, 1, 1)

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
        self.listBloodDonate.setCurrentIndex(-1)
        self.listBloodAdd.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Blood Bank Database", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFindBlood), QCoreApplication.translate("MainWindow", u"Find Blood", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Blood :", None))
        self.listBloodDonate.setItemText(0, QCoreApplication.translate("MainWindow", u"A+", None))
        self.listBloodDonate.setItemText(1, QCoreApplication.translate("MainWindow", u"A-", None))
        self.listBloodDonate.setItemText(2, QCoreApplication.translate("MainWindow", u"B+", None))
        self.listBloodDonate.setItemText(3, QCoreApplication.translate("MainWindow", u"B-", None))
        self.listBloodDonate.setItemText(4, QCoreApplication.translate("MainWindow", u"AB+", None))
        self.listBloodDonate.setItemText(5, QCoreApplication.translate("MainWindow", u"AB-", None))
        self.listBloodDonate.setItemText(6, QCoreApplication.translate("MainWindow", u"O+", None))
        self.listBloodDonate.setItemText(7, QCoreApplication.translate("MainWindow", u"O-", None))

        self.listBloodDonate.setCurrentText("")
        self.listBloodDonate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select type", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Amount :", None))
        self.inputAmountDonate.setInputMask(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_11.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDonate), QCoreApplication.translate("MainWindow", u"Donate Blood", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Age :", None))
        self.inputAgeAdd.setInputMask(QCoreApplication.translate("MainWindow", u"99", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sex :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Phone :", None))
        self.inputPhoneAdd.setInputMask(QCoreApplication.translate("MainWindow", u"9999999999", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.label_6.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blood :", None))
        self.listBloodAdd.setItemText(0, QCoreApplication.translate("MainWindow", u"A+", None))
        self.listBloodAdd.setItemText(1, QCoreApplication.translate("MainWindow", u"A-", None))
        self.listBloodAdd.setItemText(2, QCoreApplication.translate("MainWindow", u"B+", None))
        self.listBloodAdd.setItemText(3, QCoreApplication.translate("MainWindow", u"B-", None))
        self.listBloodAdd.setItemText(4, QCoreApplication.translate("MainWindow", u"AB+", None))
        self.listBloodAdd.setItemText(5, QCoreApplication.translate("MainWindow", u"AB-", None))
        self.listBloodAdd.setItemText(6, QCoreApplication.translate("MainWindow", u"O+", None))
        self.listBloodAdd.setItemText(7, QCoreApplication.translate("MainWindow", u"O-", None))

        self.listBloodAdd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAddDonor), QCoreApplication.translate("MainWindow", u"Add Donor", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

