import sqlite3 as sql
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from main_file import Ui_MainWindow_3
from lesson import Learn
from logic_2 import Logically
from tablelesson import TableLesson
from memory_training import MemoryTraining


class InTheBeginning(QMainWindow, Ui_MainWindow_3):
    def __init__(self, name='неопазнанный', email_2='aa'):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.email = email_2
        self.lesson.clicked.connect(self.run_lesson)
        self.welcome.setText(f'Здраствуйте, {self.name}')
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.additionally.clicked.connect(self.run_additional_lesson)

    def run_additional_lesson(self):
        with sql.connect("db/db_2.db") as db:
            cur = db.cursor()
            total = cur.execute("""SELECT perfect FROM date
                WHERE email = ?""", (self.email,)).fetchall()[0][0]
            db.commit()
        if int(total) >= 3:
            self.w = Logically()
            self.w.setFixedSize(800, 460)
            self.w.show()
        else:
            self.answer.setText('Этот уровень откроется при правильном прохождении 3 уроков.')

    def tabChanged(self):
        try:
            if self.tabWidget.currentIndex() == 1:
                with sql.connect("db/db_2.db") as db:
                    cur = db.cursor()
                    self.excellent.setText(str(cur.execute("""SELECT perfect 
            FROM date WHERE email = ?""", (self.email,)).fetchall()[0][0]))
                    self.total.setText(str(cur.execute("""SELECT full FROM 
            date WHERE email = ?""", (self.email,)).fetchall()[0][0]))
                db.commit()
        finally:
            pass

    def run_lesson(self):
        if self.choice.currentText() == '1 уровень':
            self.w2 = Learn(self.email, '1')
            self.w2.setFixedSize(800, 600)
            self.w2.show()
        elif self.choice.currentText() == '2 уровень':
            self.w5 = Learn(self.email, '2')
            self.w5.setFixedSize(800, 600)
            self.w5.show()
        elif self.choice.currentText() == '3 уровень':
            self.w5 = Learn(self.email, '3')
            self.w5.setFixedSize(800, 600)
            self.w5.show()
        elif self.choice.currentText() == '4 уровень':
            self.w5 = Learn(self.email, '4')
            self.w5.setFixedSize(800, 600)
            self.w5.show()
        elif self.choice.currentText() == '5 уровень':
            self.w5 = Learn(self.email, '5')
            self.w5.setFixedSize(800, 600)
            self.w5.show()
        elif self.choice.currentText() == 'Умножение':
            self.w5 = Learn(self.email, '6')
            self.w5.setFixedSize(800, 600)
            self.w5.show()
        elif self.choice.currentText() == 'Таблица Шульте':
            self.w5 = TableLesson()
            self.w5.setFixedSize(900, 650)
            self.w5.show()
        elif self.choice.currentText() == 'Тренировка памяти':
            self.w5 = MemoryTraining(self.email)
            self.w5.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InTheBeginning()
    ex.setFixedSize(660, 400)
    ex.show()
    sys.exit(app.exec_())