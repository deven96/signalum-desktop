# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './signalum.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.adapterTab = QtWidgets.QWidget()
        self.adapterTab.setObjectName("adapterTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.adapterTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.adapterTable = QtWidgets.QTableWidget(self.adapterTab)
        self.adapterTable.setObjectName("adapterTable")
        self.adapterTable.setColumnCount(2)
        self.adapterTable.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.adapterTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.adapterTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.adapterTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.adapterTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.adapterTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.adapterTable.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adapterTable.setItem(6, 0, item)
        self.adapterTable.horizontalHeader().setDefaultSectionSize(200)
        self.adapterTable.horizontalHeader().setStretchLastSection(False)
        self.adapterTable.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.adapterTable)
        self.tabWidget.addTab(self.adapterTab, "")
        self.devicesTab = QtWidgets.QWidget()
        self.devicesTab.setObjectName("devicesTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.devicesTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bluetoothTable = QtWidgets.QTableWidget(self.devicesTab)
        self.bluetoothTable.setObjectName("bluetoothTable")
        self.bluetoothTable.setColumnCount(7)
        self.bluetoothTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothTable.setHorizontalHeaderItem(6, item)
        self.bluetoothTable.horizontalHeader().setCascadingSectionResizes(False)
        self.bluetoothTable.horizontalHeader().setDefaultSectionSize(110)
        self.bluetoothTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.bluetoothTable)
        self.wifiTable = QtWidgets.QTableWidget(self.devicesTab)
        self.wifiTable.setObjectName("wifiTable")
        self.wifiTable.setColumnCount(8)
        self.wifiTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiTable.setHorizontalHeaderItem(7, item)
        self.verticalLayout_3.addWidget(self.wifiTable)
        self.tabWidget.addTab(self.devicesTab, "")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.tabWidget.addTab(self.graphTab, "")
        self.optionsTab = QtWidgets.QWidget()
        self.optionsTab.setObjectName("optionsTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.optionsTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.refreshDeviceCheckBox = QtWidgets.QCheckBox(self.optionsTab)
        self.refreshDeviceCheckBox.setObjectName("refreshDeviceCheckBox")
        self.verticalLayout_4.addWidget(self.refreshDeviceCheckBox)
        self.discoverDeviceCheckBox = QtWidgets.QCheckBox(self.optionsTab)
        self.discoverDeviceCheckBox.setObjectName("discoverDeviceCheckBox")
        self.verticalLayout_4.addWidget(self.discoverDeviceCheckBox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.optionsTab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.refreshIntervalspinBox = QtWidgets.QSpinBox(self.optionsTab)
        self.refreshIntervalspinBox.setObjectName("refreshIntervalspinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.refreshIntervalspinBox)
        self.wifiRadioButton = QtWidgets.QRadioButton(self.optionsTab)
        self.wifiRadioButton.setCheckable(True)
        self.wifiRadioButton.setChecked(False)
        self.wifiRadioButton.setObjectName("wifiRadioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wifiRadioButton)
        self.bluetoothRadioButton = QtWidgets.QRadioButton(self.optionsTab)
        self.bluetoothRadioButton.setChecked(True)
        self.bluetoothRadioButton.setAutoExclusive(False)
        self.bluetoothRadioButton.setObjectName("bluetoothRadioButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bluetoothRadioButton)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.optionsTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.adapterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.adapterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.adapterTable.isSortingEnabled()
        self.adapterTable.setSortingEnabled(False)
        item = self.adapterTable.item(0, 0)
        item.setText(_translate("MainWindow", "Vendor"))
        item = self.adapterTable.item(1, 0)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.adapterTable.item(2, 0)
        item.setText(_translate("MainWindow", "API"))
        item = self.adapterTable.item(3, 0)
        item.setText(_translate("MainWindow", "Revision"))
        item = self.adapterTable.item(4, 0)
        item.setText(_translate("MainWindow", "Services"))
        item = self.adapterTable.item(5, 0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.adapterTable.item(6, 0)
        item.setText(_translate("MainWindow", "Manufacturer"))
        self.adapterTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adapterTab), _translate("MainWindow", "Adapter Overview"))
        item = self.bluetoothTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Device"))
        item = self.bluetoothTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.bluetoothTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Manufacturer"))
        item = self.bluetoothTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Signal Strength"))
        item = self.bluetoothTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Class"))
        item = self.bluetoothTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Services"))
        item = self.bluetoothTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Details"))
        item = self.wifiTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.wifiTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.wifiTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RSSI"))
        item = self.wifiTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Frequency"))
        item = self.wifiTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quality"))
        item = self.wifiTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Encryption Type"))
        item = self.wifiTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Mode of Device"))
        item = self.wifiTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Channel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devicesTab), _translate("MainWindow", "Devices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("MainWindow", "Signal Graph"))
        self.refreshDeviceCheckBox.setText(_translate("MainWindow", "Automatically refresh device list"))
        self.discoverDeviceCheckBox.setText(_translate("MainWindow", "Dont discover services"))
        self.label_2.setText(_translate("MainWindow", "Refresh interval in millisecond"))
        self.wifiRadioButton.setText(_translate("MainWindow", "WiFi"))
        self.bluetoothRadioButton.setText(_translate("MainWindow", "Bluetooth"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), _translate("MainWindow", "Options"))


