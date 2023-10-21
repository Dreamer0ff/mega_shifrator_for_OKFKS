# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from caes import Ui_Caesar
from vizh import Ui_Vizhener
from atba import Ui_Atbash
from mors import Ui_Morse
from vernam import Vernam

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):

    def openCaesar(self):
        self.caes_window = QtWidgets.QMainWindow()
        self.ui = Ui_Caesar()
        self.ui.setupUi(self.caes_window)
        self.caes_window.show()

    def openVizhener(self):
        self.viz_window = QtWidgets.QMainWindow()
        self.ui = Ui_Vizhener()
        self.ui.setupUi(self.viz_window)
        self.viz_window.show()

    def openAtbash(self):
        self.atb_window = QtWidgets.QMainWindow()
        self.ui = Ui_Atbash()
        self.ui.setupUi(self.atb_window)
        self.atb_window.show()

    def openMorse(self):
        self.mor_window = QtWidgets.QMainWindow()
        self.ui = Ui_Morse()
        self.ui.setupUi(self.mor_window)
        self.mor_window.show()

    def openVernam(self):
        self.ver_window = QtWidgets.QMainWindow()
        self.ui = Vernam()
        self.ui.setupUi(self.ver_window)
        self.ver_window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(300, 330)
        icon = QIcon("icons/icon.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(222, 249, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 301, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Caesar_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)

        font2 = QtGui.QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)

        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Caesar_Button.setFont(font)
        self.Caesar_Button.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(0, 208, 255);\n"
"    color:  rgb(0, 0, 0);\n"
"    font-size:  20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:  rgb(60, 165, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 255, 255);\n"
"}")
        self.Caesar_Button.setCheckable(False)
        self.Caesar_Button.setObjectName("Caesar_Button")

        self.Caesar_Button.clicked.connect(self.openCaesar)

        self.verticalLayout_3.addWidget(self.Caesar_Button)
        self.Vizhener_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Vizhener_Button.setFont(font)
        self.Vizhener_Button.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(0, 208, 255);\n"
"    color:  rgb(0, 0, 0);\n"
"    font-size:  20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:  rgb(60, 165, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 255, 255);\n"
"}")
        self.Vizhener_Button.setCheckable(False)
        self.Vizhener_Button.setObjectName("Vizhener_Button")

        self.Vizhener_Button.clicked.connect(self.openVizhener)

        self.verticalLayout_3.addWidget(self.Vizhener_Button)
        self.Atbash_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Atbash_button.setFont(font)
        self.Atbash_button.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(0, 208, 255);\n"
"    color:  rgb(0, 0, 0);\n"
"    font-size:  20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:  rgb(60, 165, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 255, 255);\n"
"}")
        self.Atbash_button.setCheckable(False)
        self.Atbash_button.setObjectName("Atbash_button")

        self.Atbash_button.clicked.connect(self.openAtbash)

        self.verticalLayout_3.addWidget(self.Atbash_button)
        self.Morse_Burron = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Morse_Burron.setFont(font)
        self.Morse_Burron.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(0, 208, 255);\n"
"    color:  rgb(0, 0, 0);\n"
"    font-size:  20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:  rgb(60, 165, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 255, 255);\n"
"}")
        self.Morse_Burron.setCheckable(False)
        self.Morse_Burron.setObjectName("Morse_Burron")

        self.Morse_Burron.clicked.connect(self.openMorse)

        self.verticalLayout_3.addWidget(self.Morse_Burron)
        self.Disk_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Disk_Button.setFont(font)
        self.Disk_Button.setStyleSheet("QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(0, 208, 255);\n"
"    color:  rgb(0, 0, 0);\n"
"    font-size:  20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:  rgb(60, 165, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 255, 255);\n"
"}")
        self.Disk_Button.setCheckable(False)
        self.Disk_Button.setObjectName("Disk_Button")
        self.Disk_Button.clicked.connect(self.openVernam)
        self.verticalLayout_3.addWidget(self.Disk_Button)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.copyright = QtWidgets.QTextBrowser(self.centralwidget)
        self.copyright.setGeometry(QtCore.QRect(0, 300, 300, 31))
        self.copyright.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.copyright.setObjectName("copyright")
        self.copyright.setText("© Виноградов К.С., Шифратор, 2023")
        self.copyright.setFont(font2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифратор"))
        self.Caesar_Button.setText(_translate("MainWindow", "Шифр Цезаря"))
        self.Vizhener_Button.setText(_translate("MainWindow", "Шифр Виженера"))
        self.Atbash_button.setText(_translate("MainWindow", "Шифр Атбаш"))
        self.Morse_Burron.setText(_translate("MainWindow", "Азбука Морзе"))
        self.Disk_Button.setText(_translate("MainWindow", "Шифр Вернама"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Выберите шифратор</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())