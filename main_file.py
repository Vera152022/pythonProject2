# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'главная_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 781, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.welcome = QtWidgets.QLabel(self.tab_1)
        self.welcome.setGeometry(QtCore.QRect(490, 50, 231, 16))
        self.welcome.setObjectName("welcome")
        self.lesson = QtWidgets.QPushButton(self.tab_1)
        self.lesson.setGeometry(QtCore.QRect(300, 330, 141, 61))
        self.lesson.setObjectName("lesson")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_1)
        self.textBrowser.setGeometry(QtCore.QRect(100, 150, 551, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.choice = QtWidgets.QComboBox(self.tab_1)
        self.choice.setGeometry(QtCore.QRect(60, 40, 141, 41))
        self.choice.setObjectName("choice")
        self.choice.addItem("")
        self.choice.addItem("")
        self.choice.addItem("")
        self.choice.addItem("")
        self.choice.addItem("")
        self.choice.addItem("")
        self.additionally = QtWidgets.QPushButton(self.tab_1)
        self.additionally.setGeometry(QtCore.QRect(240, 40, 171, 41))
        self.additionally.setObjectName("additionally")
        self.answer = QtWidgets.QLabel(self.tab_1)
        self.answer.setGeometry(QtCore.QRect(130, 110, 501, 21))
        self.answer.setText("")
        self.answer.setObjectName("answer")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 271, 16))
        self.label_3.setObjectName("label_3")
        self.total = QtWidgets.QLabel(self.tab_2)
        self.total.setGeometry(QtCore.QRect(250, 100, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.excellent = QtWidgets.QLabel(self.tab_2)
        self.excellent.setGeometry(QtCore.QRect(250, 310, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.excellent.setFont(font)
        self.excellent.setObjectName("excellent")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Здраствуйте,"))
        self.lesson.setText(_translate("MainWindow", "Начать урок"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Здравствуйте, на этой вкладке вы можете порешать примеры разной сложности, выбрав уровень сложности и нажав кнопку &quot;начать урок&quot;. На вкладке &quot;Статистика&quot; вам будет предоставленна информация о ваших достижениях.</span></p></body></html>"))
        self.choice.setItemText(0, _translate("MainWindow", "1 уровень"))
        self.choice.setItemText(1, _translate("MainWindow", "2 уровень"))
        self.choice.setItemText(2, _translate("MainWindow", "Умножение"))
        self.choice.setItemText(3, _translate("MainWindow", "3 уровень"))
        self.choice.setItemText(4, _translate("MainWindow", "4 уровень"))
        self.choice.setItemText(5, _translate("MainWindow", "5 уровень"))
        self.additionally.setText(_translate("MainWindow", "Доп. уровень"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Главная страница"))
        self.label_2.setText(_translate("MainWindow", "Общее количество сделанных тестов:"))
        self.label_3.setText(_translate("MainWindow", "Количество тестов, сделанных на отлично:"))
        self.total.setText(_translate("MainWindow", "0"))
        self.excellent.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Статистика"))