# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Aug 21 11:30:47 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 497)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comport_comboBox = QtGui.QComboBox(self.groupBox)
        self.comport_comboBox.setObjectName(_fromUtf8("comport_comboBox"))
        self.verticalLayout.addWidget(self.comport_comboBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.firmwareversion_comboBox = QtGui.QComboBox(self.groupBox_2)
        self.firmwareversion_comboBox.setObjectName(_fromUtf8("firmwareversion_comboBox"))
        self.verticalLayout_3.addWidget(self.firmwareversion_comboBox)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.robotid_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.robotid_lineEdit.setObjectName(_fromUtf8("robotid_lineEdit"))
        self.horizontalLayout_2.addWidget(self.robotid_lineEdit)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.flash_pushButton = QtGui.QPushButton(self.centralwidget)
        self.flash_pushButton.setObjectName(_fromUtf8("flash_pushButton"))
        self.horizontalLayout.addWidget(self.flash_pushButton)
        self.test_pushButton = QtGui.QPushButton(self.centralwidget)
        self.test_pushButton.setObjectName(_fromUtf8("test_pushButton"))
        self.horizontalLayout.addWidget(self.test_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAoeu = QtGui.QMenu(self.menubar)
        self.menuAoeu.setObjectName(_fromUtf8("menuAoeu"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionUser_Guide = QtGui.QAction(MainWindow)
        self.actionUser_Guide.setObjectName(_fromUtf8("actionUser_Guide"))
        self.menuAoeu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menubar.addAction(self.menuAoeu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Com Port", None))
        self.label.setText(_translate("MainWindow", "Select the COM Port that the programmer is connected to.", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Firmware Version", None))
        self.label_2.setText(_translate("MainWindow", "Select the firmware version to flash. ", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Testing", None))
        self.label_3.setText(_translate("MainWindow", "Enter a remote robot\'s Serial ID to ping:", None))
        self.flash_pushButton.setText(_translate("MainWindow", "Flash", None))
        self.test_pushButton.setText(_translate("MainWindow", "Test", None))
        self.menuAoeu.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionUser_Guide.setText(_translate("MainWindow", "User Guide", None))
