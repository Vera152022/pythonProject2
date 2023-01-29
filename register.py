import sqlite3 as sql

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from registrations import Ui_MainWindow_6
from assemble import InTheBeginning
import start


class RegistrationInTheSystem(QMainWindow, Ui_MainWindow_6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_2.clicked.connect(self.run)
        self.parole.setEchoMode(QLineEdit.Password)
        self.parole_2.setEchoMode(QLineEdit.Password)
        self.back.clicked.connect(self.go_back)

    def go_back(self):
        self.w2 = start.Beginning()
        self.w2.show()
        self.close()

    def run(self):
        if self.name.text() != '' and self.age.text() != '' and \
            self.mail.text() != '' and self.parole.text() != '' \
                and self.parole_2.text() != '':
            if self.age.text().isdigit():
                if self.parole_2.text() == self.parole.text():
                    self.answer.setText('')
                    with sql.connect("db/db_2.db") as db:
                        cur = db.cursor()
                        a = [self.mail.text(), self.age.text(),
                             self.name.text(), self.parole.text()]
                        if len(cur.execute("""SELECT * FROM date
    WHERE email = ?""", (self.mail.text(), )).fetchall()) == 0:
                            cur.execute("""INSERT INTO date (email, age, 
                            name, password, full, perfect)
                             VALUES (?, ?, ?, ?, '0', '0')""", a)
                            self.w = InTheBeginning(self.name.text(),
                                              self.mail.text())
                            self.w.show()
                            self.close()
                            db.commit()
                        else:
                            self.answer.setText('Такая почта уже была '
                                                 'использованна')
                else:
                    self.answer.setText('Вы не правильно ввели пароль')
            else:
                self.answer.setText('Вы ввели в строку возраста не цифры')
        else:
            self.answer.setText('Вы не заполнили все поля регистрации')