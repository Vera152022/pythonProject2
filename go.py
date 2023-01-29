import sqlite3 as sql

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from come_in import Ui_MainWindow_2
from assemble import InTheBeginning
import start


class LogInToTheSystem(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.go.clicked.connect(self.run)
        self.password.setEchoMode(QLineEdit.Password)
        self.back.clicked.connect(self.back_2)

    def back_2(self):
        self.w2 = start.Beginning()
        self.w2.show()
        self.close()

    def run(self):
        with sql.connect("db/db_2.db") as db:
            cur = db.cursor()
            if self.email.text() != '' or self.password.text() != '':
                if len(cur.execute("""SELECT * FROM date
WHERE email = ?""", (self.email.text(),)).fetchall()) == 1:
                    if cur.execute("""SELECT password FROM date
WHERE email = ?""", (self.email.text(), )).fetchone() \
                            == (self.password.text(),):
                        self.name = cur.execute("""SELECT name FROM date
WHERE email = ?""", (self.email.text(), )).fetchone()
                        self.w = InTheBeginning(self.name[0], self.email.text())
                        self.w.show()
                        self.close()
                        db.commit()
                    else:
                        self.label_3.setText('Введен не правеньный пароль')
                else:
                    self.label_3.setText('Такая почта не была '
                                         'зарегистривованна')
            else:
                self.label_3.setText('Вы ничего не ввели в поля')
