from PyQt5.QtWidgets import QMainWindow, QInputDialog

import lesson
from memoryLevel_design import Ui_MainWindow
import lesson
import random
import sqlite3 as sql


class MemoryTraining(QMainWindow, Ui_MainWindow):
    def __init__(self, email='aa'):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.words = list(map(lambda x: x[:-1], open('slovar.txt', encoding="utf-8").readlines()))
        self.s = 0
        self.email = email
        self.mistakes = 0
        random.shuffle(self.words)
        self.pushButton.setText("Продолжить")
        for i in range(5):
            eval(f'self.label_{i + 1}.setText("{self.words[i]}")')
            eval(f'self.lineEdit_{i + 1}.setEnabled(False)')

    def start(self):
        if self.s == 0:
            for i in range(5):
                eval(f'self.label_{i + 1}.setText("")')
                eval(f'self.lineEdit_{i + 1}.setEnabled(True)')
            self.pushButton.setText("Проверить")
            self.label_6.setText('')
            self.s += 1
        elif self.s == 1:
            w = self.words[:5]
            for i in range(5):
                if not self.kostyl(eval(f'self.lineEdit_{i + 1}.text()')) in w:
                    if eval(f'self.lineEdit_{i + 1}.text()') == '':
                        eval(f'self.lineEdit_{i + 1}.setText("Нет ответа")')
                    self.mistakes += 1
                else:
                    w.remove(self.kostyl(eval(f'self.lineEdit_{i + 1}.text()')))
                eval(f'self.lineEdit_{i + 1}.setEnabled(False)')
            self.pushButton.setText("Завершить")
            if self.mistakes == 0:
                self.label_6.setText('Всё правильно! Вы молодец!')
            else:
                if self.mistakes == 1:
                    word = 'слове'
                else:
                    word = 'словах'
                self.label_6.setText(f'Ой, вы ошиблись только в {self.mistakes} {word}. В следующий раз всё получится!')
            self.s = -1
            self.perfect = 1
            self.adds()
        elif self.s == -1:
            self.close()
            self.adds()

    def adds(self):
        with sql.connect("db/db_2.db") as db:
            cur = db.cursor()
            self.full = int(cur.execute("""SELECT full FROM date
                    WHERE email = ?""", (self.email,)).fetchall()[0][0]) + 1
            self.perfect = int(cur.execute("""SELECT perfect FROM date
            WHERE email = ?""", (self.email,)).fetchall()[0][0]) + self.perfect
            cur.execute("""UPDATE date SET full=? WHERE email=?""",
                        (self.full, self.email,))
            cur.execute("""UPDATE date SET perfect=? WHERE email=?""",
                        (self.perfect, self.email,))
        db.commit()

    def kostyl(self, word):
        f = ''
        for e in list(word):
            if e == 'ё':
                f += 'е'
            else:
                f += e
        return f
