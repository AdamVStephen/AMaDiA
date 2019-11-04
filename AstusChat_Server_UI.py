# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AstusChat_Server_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerInterface(object):
    def setupUi(self, ServerInterface):
        ServerInterface.setObjectName("ServerInterface")
        ServerInterface.resize(983, 668)
        self.centralwidget = QtWidgets.QWidget(ServerInterface)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ChatDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.ChatDisplay.setObjectName("ChatDisplay")
        self.gridLayout.addWidget(self.ChatDisplay, 2, 6, 1, 12)
        self.OnlineList = QtWidgets.QListWidget(self.centralwidget)
        self.OnlineList.setAutoScroll(False)
        self.OnlineList.setObjectName("OnlineList")
        self.gridLayout.addWidget(self.OnlineList, 1, 0, 2, 5)
        self.PortField = QtWidgets.QLineEdit(self.centralwidget)
        self.PortField.setAutoFillBackground(True)
        self.PortField.setInputMask("")
        self.PortField.setObjectName("PortField")
        self.gridLayout.addWidget(self.PortField, 1, 8, 1, 1, QtCore.Qt.AlignLeft)
        self.FontSizeBox = QtWidgets.QSpinBox(self.centralwidget)
        self.FontSizeBox.setMinimum(6)
        self.FontSizeBox.setMaximum(18)
        self.FontSizeBox.setProperty("value", 9)
        self.FontSizeBox.setObjectName("FontSizeBox")
        self.gridLayout.addWidget(self.FontSizeBox, 1, 13, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 10, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 6, 1, 1)
        self.MuteButton = QtWidgets.QPushButton(self.centralwidget)
        self.MuteButton.setObjectName("MuteButton")
        self.gridLayout.addWidget(self.MuteButton, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 14, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 15, 1, 2)
        self.IPField = QtWidgets.QLineEdit(self.centralwidget)
        self.IPField.setAutoFillBackground(True)
        self.IPField.setInputMask("")
        self.IPField.setText("")
        self.IPField.setObjectName("IPField")
        self.gridLayout.addWidget(self.IPField, 1, 7, 1, 1)
        self.FontText = QtWidgets.QLabel(self.centralwidget)
        self.FontText.setObjectName("FontText")
        self.gridLayout.addWidget(self.FontText, 1, 11, 1, 1)
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setObjectName("SendButton")
        self.gridLayout.addWidget(self.SendButton, 3, 17, 1, 1)
        self.ConnectCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ConnectCheckBox.setObjectName("ConnectCheckBox")
        self.gridLayout.addWidget(self.ConnectCheckBox, 1, 9, 1, 1)
        self.BanButton = QtWidgets.QPushButton(self.centralwidget)
        self.BanButton.setObjectName("BanButton")
        self.gridLayout.addWidget(self.BanButton, 3, 1, 1, 1)
        self.KickButton = QtWidgets.QPushButton(self.centralwidget)
        self.KickButton.setObjectName("KickButton")
        self.gridLayout.addWidget(self.KickButton, 3, 2, 1, 1)
        self.InputField = QtWidgets.QLineEdit(self.centralwidget)
        self.InputField.setAutoFillBackground(True)
        self.InputField.setObjectName("InputField")
        self.gridLayout.addWidget(self.InputField, 3, 6, 1, 11)
        ServerInterface.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ServerInterface)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 21))
        self.menubar.setObjectName("menubar")
        ServerInterface.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ServerInterface)
        self.statusbar.setObjectName("statusbar")
        ServerInterface.setStatusBar(self.statusbar)

        self.retranslateUi(ServerInterface)
        QtCore.QMetaObject.connectSlotsByName(ServerInterface)

    def retranslateUi(self, ServerInterface):
        _translate = QtCore.QCoreApplication.translate
        ServerInterface.setWindowTitle(_translate("ServerInterface", "Chat Server by Astus"))
        self.PortField.setPlaceholderText(_translate("ServerInterface", "Port"))
        self.MuteButton.setText(_translate("ServerInterface", "Mute"))
        self.IPField.setPlaceholderText(_translate("ServerInterface", "IP"))
        self.FontText.setText(_translate("ServerInterface", "Set Font Size"))
        self.SendButton.setText(_translate("ServerInterface", "Send"))
        self.ConnectCheckBox.setText(_translate("ServerInterface", "SetUp"))
        self.BanButton.setText(_translate("ServerInterface", "Ban"))
        self.KickButton.setText(_translate("ServerInterface", "Kick"))
        self.InputField.setPlaceholderText(_translate("ServerInterface", "Message"))

