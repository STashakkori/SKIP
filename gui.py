# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 693)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(110, 4, 111, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/nasalogo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(4, 0, 101, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/spaceAppsLogo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 225, 101))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 59, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 61, 16))
        self.label_6.setObjectName("label_6")
        self.lat_box = QtWidgets.QLineEdit(self.centralWidget)
        self.lat_box.setGeometry(QtCore.QRect(80, 220, 113, 21))
        self.lat_box.setObjectName("lat_box")
        self.long_box = QtWidgets.QLineEdit(self.centralWidget)
        self.long_box.setGeometry(QtCore.QRect(80, 250, 113, 21))
        self.long_box.setObjectName("long_box")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(30, 290, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.panel_combo = QtWidgets.QComboBox(self.centralWidget)
        self.panel_combo.setGeometry(QtCore.QRect(60, 320, 141, 26))
        self.panel_combo.setCurrentText("")
        self.panel_combo.setObjectName("panel_combo")
        self.panel_combo.addItem("")
        self.panel_combo.addItem("")
        self.panel_combo.addItem("")
        self.panel_combo.addItem("")
        self.panel_combo.addItem("")
        self.panel_combo.addItem("")
        self.panel_combo.addItem("")
        self.panel_combo.setItemText(6, "")
        self.panel_box = QtWidgets.QLineEdit(self.centralWidget)
        self.panel_box.setGeometry(QtCore.QRect(70, 360, 113, 21))
        self.panel_box.setObjectName("panel_box")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(10, 360, 51, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(10, 320, 41, 20))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(90, 440, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.item_combo = QtWidgets.QComboBox(self.centralWidget)
        self.item_combo.setGeometry(QtCore.QRect(9, 470, 211, 26))
        self.item_combo.setObjectName("item_combo")
        self.item_combo.addItem("")
        self.item_combo.setItemText(0, "")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setGeometry(QtCore.QRect(10, 510, 71, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(120, 510, 71, 20))
        self.label_12.setObjectName("label_12")
        self.start_box = QtWidgets.QLineEdit(self.centralWidget)
        self.start_box.setGeometry(QtCore.QRect(10, 540, 81, 21))
        self.start_box.setObjectName("start_box")
        self.stop_box = QtWidgets.QLineEdit(self.centralWidget)
        self.stop_box.setGeometry(QtCore.QRect(120, 540, 81, 21))
        self.stop_box.setObjectName("stop_box")
        self.add_button = QtWidgets.QPushButton(self.centralWidget)
        self.add_button.setGeometry(QtCore.QRect(70, 570, 61, 32))
        self.add_button.setObjectName("add_button")
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setGeometry(QtCore.QRect(0, 140, 225, 41))
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet("")
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.centralWidget)
        self.label_17.setGeometry(QtCore.QRect(10, 153, 91, 16))
        self.label_17.setObjectName("label_17")
        self.date_box = QtWidgets.QLineEdit(self.centralWidget)
        self.date_box.setGeometry(QtCore.QRect(100, 150, 113, 21))
        self.date_box.setObjectName("date_box")
        self.label_18 = QtWidgets.QLabel(self.centralWidget)
        self.label_18.setGeometry(QtCore.QRect(0, 600, 831, 71))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet("background:transparent")
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(340, 610, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralWidget)
        self.label_20.setGeometry(QtCore.QRect(10, 640, 81, 16))
        self.label_20.setObjectName("label_20")
        self.temp_box = QtWidgets.QLineEdit(self.centralWidget)
        self.temp_box.setGeometry(QtCore.QRect(90, 640, 41, 21))
        self.temp_box.setObjectName("temp_box")
        self.label_21 = QtWidgets.QLabel(self.centralWidget)
        self.label_21.setGeometry(QtCore.QRect(190, 640, 81, 16))
        self.label_21.setObjectName("label_21")
        self.press_box = QtWidgets.QLineEdit(self.centralWidget)
        self.press_box.setGeometry(QtCore.QRect(250, 640, 41, 21))
        self.press_box.setObjectName("press_box")
        self.label_22 = QtWidgets.QLabel(self.centralWidget)
        self.label_22.setGeometry(QtCore.QRect(340, 640, 81, 16))
        self.label_22.setObjectName("label_22")
        self.humid_box = QtWidgets.QLineEdit(self.centralWidget)
        self.humid_box.setGeometry(QtCore.QRect(400, 640, 41, 21))
        self.humid_box.setObjectName("humid_box")
        self.label_23 = QtWidgets.QLabel(self.centralWidget)
        self.label_23.setGeometry(QtCore.QRect(500, 640, 81, 16))
        self.label_23.setObjectName("label_23")
        self.wind_box = QtWidgets.QLineEdit(self.centralWidget)
        self.wind_box.setGeometry(QtCore.QRect(580, 640, 41, 21))
        self.wind_box.setObjectName("wind_box")
        self.label_24 = QtWidgets.QLabel(self.centralWidget)
        self.label_24.setGeometry(QtCore.QRect(670, 640, 91, 16))
        self.label_24.setObjectName("label_24")
        self.wind_box_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.wind_box_2.setGeometry(QtCore.QRect(770, 640, 41, 21))
        self.wind_box_2.setObjectName("wind_box_2")
        self.label_25 = QtWidgets.QLabel(self.centralWidget)
        self.label_25.setGeometry(QtCore.QRect(0, 100, 121, 41))
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet("background:transparent")
        self.label_25.setFrameShape(QtWidgets.QFrame.Box)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.earth_button = QtWidgets.QPushButton(self.centralWidget)
        self.earth_button.setGeometry(QtCore.QRect(0, 107, 61, 32))
        self.earth_button.setObjectName("earth_button")
        self.mars_button = QtWidgets.QPushButton(self.centralWidget)
        self.mars_button.setGeometry(QtCore.QRect(60, 107, 61, 32))
        self.mars_button.setObjectName("mars_button")
        self.help_button = QtWidgets.QPushButton(self.centralWidget)
        self.help_button.setGeometry(QtCore.QRect(140, 107, 71, 32))
        self.help_button.setObjectName("help_button")
        self.label_27 = QtWidgets.QLabel(self.centralWidget)
        self.label_27.setGeometry(QtCore.QRect(0, 430, 225, 171))
        self.label_27.setAutoFillBackground(False)
        self.label_27.setStyleSheet("background:transparent")
        self.label_27.setFrameShape(QtWidgets.QFrame.Box)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.centralWidget)
        self.label_29.setGeometry(QtCore.QRect(0, 180, 225, 251))
        self.label_29.setAutoFillBackground(False)
        self.label_29.setStyleSheet("background:transparent")
        self.label_29.setFrameShape(QtWidgets.QFrame.Box)
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.label_26 = QtWidgets.QLabel(self.centralWidget)
        self.label_26.setGeometry(QtCore.QRect(120, 100, 105, 41))
        self.label_26.setAutoFillBackground(False)
        self.label_26.setStyleSheet("background:transparent")
        self.label_26.setFrameShape(QtWidgets.QFrame.Box)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.comp_button = QtWidgets.QPushButton(self.centralWidget)
        self.comp_button.setGeometry(QtCore.QRect(45, 397, 131, 32))
        self.comp_button.setObjectName("comp_button")
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(410, 260, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_18.raise_()
        self.label_27.raise_()
        self.label_29.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.lat_box.raise_()
        self.long_box.raise_()
        self.label_7.raise_()
        self.panel_combo.raise_()
        self.panel_box.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_8.raise_()
        self.item_combo.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.start_box.raise_()
        self.stop_box.raise_()
        self.add_button.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.date_box.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.temp_box.raise_()
        self.label_21.raise_()
        self.press_box.raise_()
        self.label_22.raise_()
        self.humid_box.raise_()
        self.label_23.raise_()
        self.wind_box.raise_()
        self.label_24.raise_()
        self.wind_box_2.raise_()
        self.earth_button.raise_()
        self.mars_button.raise_()
        self.help_button.raise_()
        self.comp_button.raise_()
        self.label_13.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 831, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuSpace_Apps_Challenge = QtWidgets.QMenu(self.menuBar)
        self.menuSpace_Apps_Challenge.setObjectName("menuSpace_Apps_Challenge")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuSpace_Apps_Challenge.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SKIP 1.0"))
        self.label_4.setText(_translate("MainWindow", "Location"))
        self.label_5.setText(_translate("MainWindow", "Latitude"))
        self.label_6.setText(_translate("MainWindow", "Longitude"))
        self.label_7.setText(_translate("MainWindow", "Solar Panel Efficiency"))
        self.panel_combo.setItemText(0, _translate("MainWindow", "Monocrystalline"))
        self.panel_combo.setItemText(1, _translate("MainWindow", "Galium Arsenide"))
        self.panel_combo.setItemText(2, _translate("MainWindow", "Polycrystalline"))
        self.panel_combo.setItemText(3, _translate("MainWindow", "Amorphous"))
        self.panel_combo.setItemText(4, _translate("MainWindow", "CdTe"))
        self.panel_combo.setItemText(5, _translate("MainWindow", "CIS/CIGS"))
        self.label_9.setText(_translate("MainWindow", "Manual"))
        self.label_10.setText(_translate("MainWindow", "Preset"))
        self.label_8.setText(_translate("MainWindow", "Item"))
        self.label_11.setText(_translate("MainWindow", "Start Time"))
        self.label_12.setText(_translate("MainWindow", "Stop Time"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.label_17.setText(_translate("MainWindow", "Today\'s date:"))
        self.label_19.setText(_translate("MainWindow", "Weather Report"))
        self.label_20.setText(_translate("MainWindow", "Temperature"))
        self.label_21.setText(_translate("MainWindow", "Pressure"))
        self.label_22.setText(_translate("MainWindow", "Humidity"))
        self.label_23.setText(_translate("MainWindow", "Wind Speed"))
        self.label_24.setText(_translate("MainWindow", "Wind Direction"))
        self.earth_button.setText(_translate("MainWindow", "Earth"))
        self.mars_button.setText(_translate("MainWindow", "Mars"))
        self.help_button.setText(_translate("MainWindow", "HELP?!"))
        self.comp_button.setText(_translate("MainWindow", "Compute Power"))
        self.label_13.setText(_translate("MainWindow", "To be released in SKIP 2.0"))
        self.menuSpace_Apps_Challenge.setTitle(_translate("MainWindow", "Space Apps Challenge"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

