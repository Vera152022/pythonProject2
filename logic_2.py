from PyQt5.QtWidgets import QMainWindow, QInputDialog
from logic import Ui_MainWindow_5
from PyQt5.QtGui import QIntValidator
from pictere_2 import Pictures


class Logically(QMainWindow, Ui_MainWindow_5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer.setValidator(QIntValidator())
        self.check.clicked.connect(self.question)

    def question(self):
        name, ok_pressed = QInputDialog.getItem(self, "подтвердите ответ",
    "Вы уверенны, что хотите отправить ответ?", ("Да", "Нет"), 1, False)
        if name == 'Да':
            self.answer_total()

    def answer_total(self):
        if self.answer.text() == '10':
            self.mistake.setText('Молодец! Ты нашел правильное решение.')
            self.w = Pictures(3)
            self.w.show()
        else:
            self.w = Pictures(4)
            self.w.show()
            self.mistake.setText('Упс, что-то пошло не так. Ответ неверен.')