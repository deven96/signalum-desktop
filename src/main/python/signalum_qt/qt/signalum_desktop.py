# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './signalum_desktop.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.adapterTab = QtWidgets.QWidget()
        self.adapterTab.setObjectName("adapterTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.adapterTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.adapterTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.bluetoothAdapterTable = QtWidgets.QTableWidget(self.adapterTab)
        self.bluetoothAdapterTable.setObjectName("bluetoothAdapterTable")
        self.bluetoothAdapterTable.setColumnCount(2)
        self.bluetoothAdapterTable.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.bluetoothAdapterTable.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bluetoothAdapterTable.setItem(6, 0, item)
        self.bluetoothAdapterTable.horizontalHeader().setDefaultSectionSize(200)
        self.bluetoothAdapterTable.horizontalHeader().setStretchLastSection(False)
        self.bluetoothAdapterTable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.bluetoothAdapterTable)
        self.label = QtWidgets.QLabel(self.adapterTab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.wifiAdapterTable = QtWidgets.QTableWidget(self.adapterTab)
        self.wifiAdapterTable.setObjectName("wifiAdapterTable")
        self.wifiAdapterTable.setColumnCount(2)
        self.wifiAdapterTable.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.wifiAdapterTable.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wifiAdapterTable.setItem(6, 0, item)
        self.wifiAdapterTable.horizontalHeader().setDefaultSectionSize(200)
        self.wifiAdapterTable.horizontalHeader().setStretchLastSection(False)
        self.wifiAdapterTable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.wifiAdapterTable)
        self.tabWidget.addTab(self.adapterTab, "")
        self.devicesTab = QtWidgets.QWidget()
        self.devicesTab.setObjectName("devicesTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.devicesTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bluetoothTable = QtWidgets.QTableWidget(self.devicesTab)
        self.bluetoothTable.setObjectName("bluetoothTable")
        self.bluetoothTable.setColumnCount(6)
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
        self.wifiTable.horizontalHeader().setCascadingSectionResizes(True)
        self.wifiTable.horizontalHeader().setDefaultSectionSize(110)
        self.wifiTable.horizontalHeader().setStretchLastSection(True)
        self.wifiTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.wifiTable)
        self.tabWidget.addTab(self.devicesTab, "")
        self.graphTab = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.graphTab.setPalette(palette)
        self.graphTab.setObjectName("graphTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.graphTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(self.graphTab)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.bluetoothGraphLayout = QtWidgets.QVBoxLayout()
        self.bluetoothGraphLayout.setObjectName("bluetoothGraphLayout")
        self.verticalLayout_6.addLayout(self.bluetoothGraphLayout)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.bluetoothGraphToolbar = QtWidgets.QVBoxLayout()
        self.bluetoothGraphToolbar.setObjectName("bluetoothGraphToolbar")
        self.verticalLayout_6.addLayout(self.bluetoothGraphToolbar)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.wifiGraphLayout = QtWidgets.QVBoxLayout()
        self.wifiGraphLayout.setObjectName("wifiGraphLayout")
        self.verticalLayout_6.addLayout(self.wifiGraphLayout)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_6.addWidget(self.line_5)
        self.wifiGraphToolbar = QtWidgets.QVBoxLayout()
        self.wifiGraphToolbar.setObjectName("wifiGraphToolbar")
        self.verticalLayout_6.addLayout(self.wifiGraphToolbar)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addWidget(self.widget)
        self.tabWidget.addTab(self.graphTab, "")
        self.optionsTab = QtWidgets.QWidget()
        self.optionsTab.setObjectName("optionsTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.optionsTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_15)
        self.label_6 = QtWidgets.QLabel(self.optionsTab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.showBluetoothServices = QtWidgets.QCheckBox(self.optionsTab)
        self.showBluetoothServices.setObjectName("showBluetoothServices")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.showBluetoothServices)
        self.showBluetoothNames = QtWidgets.QCheckBox(self.optionsTab)
        self.showBluetoothNames.setChecked(True)
        self.showBluetoothNames.setObjectName("showBluetoothNames")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.showBluetoothNames)
        self.label_2 = QtWidgets.QLabel(self.optionsTab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.bluetoothRefreshRate = QtWidgets.QSpinBox(self.optionsTab)
        self.bluetoothRefreshRate.setMinimum(1000)
        self.bluetoothRefreshRate.setMaximum(10000)
        self.bluetoothRefreshRate.setSingleStep(50)
        self.bluetoothRefreshRate.setObjectName("bluetoothRefreshRate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bluetoothRefreshRate)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.optionsTab)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_7 = QtWidgets.QLabel(self.optionsTab)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.wifiRefreshRate = QtWidgets.QSpinBox(self.optionsTab)
        self.wifiRefreshRate.setMinimum(1000)
        self.wifiRefreshRate.setMaximum(10000)
        self.wifiRefreshRate.setSingleStep(50)
        self.wifiRefreshRate.setObjectName("wifiRefreshRate")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.wifiRefreshRate)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_19)
        self.label_9 = QtWidgets.QLabel(self.optionsTab)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.wifiSwitch = QtWidgets.QCheckBox(self.optionsTab)
        self.wifiSwitch.setEnabled(True)
        self.wifiSwitch.setChecked(True)
        self.wifiSwitch.setObjectName("wifiSwitch")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.wifiSwitch)
        self.checkBox_3 = QtWidgets.QCheckBox(self.optionsTab)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.optionsTab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_5.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.optionsTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 22))
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
        self.label_3.setText(_translate("MainWindow", "Wifi Adapter"))
        item = self.bluetoothAdapterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.bluetoothAdapterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.bluetoothAdapterTable.isSortingEnabled()
        self.bluetoothAdapterTable.setSortingEnabled(False)
        item = self.bluetoothAdapterTable.item(0, 0)
        item.setText(_translate("MainWindow", "Vendor"))
        item = self.bluetoothAdapterTable.item(1, 0)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.bluetoothAdapterTable.item(2, 0)
        item.setText(_translate("MainWindow", "API"))
        item = self.bluetoothAdapterTable.item(3, 0)
        item.setText(_translate("MainWindow", "Revision"))
        item = self.bluetoothAdapterTable.item(4, 0)
        item.setText(_translate("MainWindow", "Services"))
        item = self.bluetoothAdapterTable.item(5, 0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.bluetoothAdapterTable.item(6, 0)
        item.setText(_translate("MainWindow", "Manufacturer"))
        self.bluetoothAdapterTable.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Bluetooth Adapter"))
        item = self.wifiAdapterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.wifiAdapterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.wifiAdapterTable.isSortingEnabled()
        self.wifiAdapterTable.setSortingEnabled(False)
        item = self.wifiAdapterTable.item(0, 0)
        item.setText(_translate("MainWindow", "Vendor"))
        item = self.wifiAdapterTable.item(1, 0)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.wifiAdapterTable.item(2, 0)
        item.setText(_translate("MainWindow", "API"))
        item = self.wifiAdapterTable.item(3, 0)
        item.setText(_translate("MainWindow", "Revision"))
        item = self.wifiAdapterTable.item(4, 0)
        item.setText(_translate("MainWindow", "Services"))
        item = self.wifiAdapterTable.item(5, 0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.wifiAdapterTable.item(6, 0)
        item.setText(_translate("MainWindow", "Manufacturer"))
        self.wifiAdapterTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adapterTab), _translate("MainWindow", "Adapter Overview"))
        self.bluetoothTable.setSortingEnabled(True)
        item = self.bluetoothTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Device"))
        item = self.bluetoothTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC Address"))
        item = self.bluetoothTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Signal Strength"))
        item = self.bluetoothTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Major Class"))
        item = self.bluetoothTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Minor Class"))
        item = self.bluetoothTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Services"))
        self.wifiTable.setSortingEnabled(True)
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
        self.label_5.setText(_translate("MainWindow", "Bluetooth Devices"))
        self.label_4.setText(_translate("MainWindow", "Wifi Devices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("MainWindow", "Signal Graph"))
        self.label_6.setText(_translate("MainWindow", "Bluetooth"))
        self.showBluetoothServices.setText(_translate("MainWindow", "Show bluetooth services"))
        self.showBluetoothNames.setText(_translate("MainWindow", "Show bluetooth names"))
        self.label_2.setText(_translate("MainWindow", "Refresh rate (ms)"))
        self.label_8.setText(_translate("MainWindow", "Wifi"))
        self.label_7.setText(_translate("MainWindow", "Refresh rate (ms)"))
        self.label_9.setText(_translate("MainWindow", "All"))
        self.wifiSwitch.setText(_translate("MainWindow", "Turn Wifi on"))
        self.checkBox_3.setText(_translate("MainWindow", "Turn Bluetooth on"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), _translate("MainWindow", "Options"))

