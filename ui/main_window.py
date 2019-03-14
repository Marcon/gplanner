# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Wed Mar 13 16:55:42 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout.addWidget(self.treeWidget)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.fiberLengthSpin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.fiberLengthSpin.setObjectName("fiberLengthSpin")
        self.gridLayout_2.addWidget(self.fiberLengthSpin, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.splitterTypeCombo = QtWidgets.QComboBox(self.centralwidget)
        self.splitterTypeCombo.setObjectName("splitterTypeCombo")
        self.gridLayout_2.addWidget(self.splitterTypeCombo, 0, 1, 1, 1)
        self.addSplitterButton = QtWidgets.QPushButton(self.centralwidget)
        self.addSplitterButton.setObjectName("addSplitterButton")
        self.gridLayout_2.addWidget(self.addSplitterButton, 0, 2, 1, 1)
        self.deleteSplitterButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteSplitterButton.setObjectName("deleteSplitterButton")
        self.gridLayout_2.addWidget(self.deleteSplitterButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Type", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "Signal attenuation", None, -1))
        self.treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("MainWindow", "Fiber length", None, -1))
        self.treeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("MainWindow", "Free connectors", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Equipment type", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Fiber length(km)", None, -1))
        self.addSplitterButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add Equipment", None, -1))
        self.deleteSplitterButton.setText(QtWidgets.QApplication.translate("MainWindow", "Delete Equipment", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "F&ile", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "&Exit", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "&Save", None, -1))
        self.actionSave_as.setText(QtWidgets.QApplication.translate("MainWindow", "Save &as", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "&Open", None, -1))

