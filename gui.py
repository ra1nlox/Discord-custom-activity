# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(365, 93)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.submit_button.setObjectName("submit_button")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(270, 30, 75, 23))
        self.reset_button.setObjectName("reset_button")
        self.Enter_name_label = QtWidgets.QLabel(self.centralwidget)
        self.Enter_name_label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.Enter_name_label.setObjectName("Enter_name_label")
        self.show_help_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_help_button.setGeometry(QtCore.QRect(10, 60, 71, 23))
        self.show_help_button.setObjectName("pushButton")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate(
            "MainWindow", "Discord custom game activity"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.Enter_name_label.setText(_translate("MainWindow", "Enter name:"))
        self.show_help_button.setText(_translate("MainWindow", "Help"))
