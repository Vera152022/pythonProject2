# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'анкета.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont


class Ui_MainWindow_6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 30, 700, 700))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(260, 140, 241, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mail = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.mail.setObjectName("mail")
        self.verticalLayout_4.addWidget(self.mail)
        self.parole = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.parole.setObjectName("parole")
        self.verticalLayout_4.addWidget(self.parole)
        self.parole_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.parole_2.setObjectName("parole_2")
        self.verticalLayout_4.addWidget(self.parole_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 140, 250, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.register_2 = QtWidgets.QPushButton(self.groupBox)
        self.register_2.setGeometry(QtCore.QRect(150, 290, 300, 41))
        self.register_2.setObjectName("register_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 50, 241, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.name.setObjectName("name")
        self.verticalLayout_2.addWidget(self.name)
        self.age = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.age.setObjectName("age")
        self.verticalLayout_2.addWidget(self.age)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 101, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.answer = QtWidgets.QLabel(self.groupBox)
        self.answer.setGeometry(QtCore.QRect(70, 250, 600, 41))
        self.answer.setText("")
        self.answer.setObjectName("answer")
        self.back = QtWidgets.QPushButton(self.groupBox)
        self.back.setGeometry(QtCore.QRect(150, 340, 300, 41))
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 41))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.register_2, self.mail)
        MainWindow.setTabOrder(self.mail, self.parole)
        MainWindow.setTabOrder(self.parole, self.parole_2)

        self.groupBox.setFont(QFont('Dosis', 15))
        self.label_3.setFont(QFont('Dosis', 15))
        self.label_4.setFont(QFont('Dosis', 15))
        self.label_6.setFont(QFont('Dosis', 15))
        self.register_2.setFont(QFont('Dosis', 15))
        self.label.setFont(QFont('Dosis', 15))
        self.label_2.setFont(QFont('Dosis', 15))
        self.back.setFont(QFont('Dosis', 15))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Анкета:"))
        self.label_3.setText(_translate("MainWindow", "Почта:"))
        self.label_4.setText(_translate("MainWindow", "Придумайте пароль:"))
        self.label_6.setText(_translate("MainWindow", "Повторите пароль:"))
        self.register_2.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.label.setText(_translate("MainWindow", "Имя:"))
        self.label_2.setText(_translate("MainWindow", "Возраст:"))
        self.back.setText(_translate("MainWindow", "Назад"))
