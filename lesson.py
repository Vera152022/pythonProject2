import random
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

from PyQt5.QtWidgets import QMainWindow
from lesson_2 import Ui_MainWindow_4
import sqlite3 as sql
from PyQt5.QtGui import QIntValidator
from pictere_2 import Pictures


class Learn(QMainWindow, Ui_MainWindow_4):
    def __init__(self, email='aa', flag='5'):
        super().__init__()
        self.setupUi(self)
        self.dictionary = {}
        self.flag = flag
        self.email = email
        self.stop = 0
        self.perfect = 0
        self.full = 0
        self.start()

    def start(self):
        if self.flag == '1':
            for i in range(1, 21):
                eval(f'self.answer_{i}.setValidator(QIntValidator())')
                number = random.randint(1, 100)
                number_2 = random.randint(1, 100)
                if i % 2 == 0:
                    self.dictionary[i] = number + number_2
                    eval(f'self.text_{i}.setText("{number} + {number_2} '
                         f'= ")')
                if i % 2 == 1:
                    if number <= number_2:
                        self.dictionary[i] = number_2 - number
                        eval(f'self.text_{i}.setText("{number_2} - {number} '
                             f'= ")')
                    else:
                        self.dictionary[i] = number - number_2
                        eval(f'self.text_{i}.setText("{number} - {number_2} '
                             f'= ")')
        if self.flag == '2':
            for i in range(1, 21):
                eval(f'self.answer_{i}.setValidator(QIntValidator())')
                number = random.randint(1, 10)
                if i % 2 == 0:
                    number_2 = random.randint(1, 10)
                    self.dictionary[i] = number * number_2
                    eval(f'self.text_{i}.setText("{number} * {number_2} '
                         f'= ")')
                if i % 2 == 1:
                    number_2 = random.randint(1, 100)
                    if number_2 % number == 0 and number <= number_2:
                        self.dictionary[i] = number_2 // number
                        eval(f'self.text_{i}.setText("{number_2} ÷ {number}'
                             f' = ")')
                    else:
                        number_2 = number_2 + (number - (number_2 % number))
                        self.dictionary[i] = number_2 // number
                        eval(f'self.text_{i}.setText("{number_2} ÷ {number}'
                             f' = ")')
        if self.flag == '3':
            for i in range(1, 21):
                eval(f'self.answer_{i}.setValidator(QIntValidator())')
                number = random.randint(1, 10)
                number_2 = random.randint(1, 10)
                number_3 = random.randint(1, 10)
                if i % 2 == 0:
                    self.dictionary[i] = number_2 * number_3 + number
                    eval(f'self.text_{i}.setText("{number} + {number_2} * '
                         f'{number_3} = ")')
                if i % 2 == 1:
                    self.dictionary[i] = number_2 * number_3 - number
                    eval(f'self.text_{i}.setText("{number_2} * {number_3} -'
                         f' {number} = ")')
        if self.flag == '4':
            for i in range(1, 21):
                eval(f'self.answer_{i}.setValidator(QIntValidator())')
                number = random.randint(1, 10)
                number_2 = random.randint(1, 10)
                number_3 = random.randint(1, 10)
                if i % 2 == 1:
                    if number % number_2 == 0:
                        self.dictionary[i] = number // number_2 + number_3
                        eval(f'self.text_{i}.setText("{number_3} + {number}'
                             f' ÷ {number_2} = ")')
                    else:
                        number = number + (number_2 - (number % number_2))
                        self.dictionary[i] = number // number_2 + number_3
                        eval(f'self.text_{i}.setText("{number_3} + {number}'
                             f' ÷ {number_2} = ")')
                else:
                    if number % number_2 == 0:
                        if number % number_2 > number_3:
                            self.dictionary[i] = number // number_2 - number_3
                            eval(f'self.text_{i}.setText("{number} ÷ '
                                 f'{number_2} - {number_3} = ")')
                        else:
                            self.dictionary[i] = number_3 - number // number_2
                            eval(f'self.text_{i}.setText("{number_3} - '
                                 f'{number} ÷ {number_2} = ")')
                    else:
                        number = number + (number_2 - (number % number_2))
                        if number % number_2 > number_3:
                            self.dictionary[i] = number // number_2 - number_3
                            eval(f'self.text_{i}.setText("{number} ÷ '
                                 f'{number_2} - {number_3} = ")')
                        else:
                            self.dictionary[i] = number_3 - number // number_2
                            eval(f'self.text_{i}.setText("{number_3} - '
                                 f'{number} ÷ {number_2} = ")')
        if self.flag == '5':
            for i in range(1, 21):
                eval(f'self.answer_{i}.setValidator(QIntValidator())')
                number = random.randint(1, 10)
                number_2 = random.randint(1, 10)
                number_3 = random.randint(1, 10)
                if i % 2 == 0:
                    self.dictionary[i] = number_2 * number_3 * number
                    eval(f'self.text_{i}.setText("{number} * {number_2} * '
                         f'{number_3} = ")')
                if i % 2 == 1:
                    if number * number_2 % number_3 == 0:
                        self.dictionary[i] = number * number_2 // number_3
                        eval(f'self.text_{i}.setText("{number} * '
                             f'{number_2} ÷ {number_3} = ")')
                    else:
                        number_3 = 2
                        while number_3 <= number * number_2:
                            if number * number_2 % number_3 == 0:
                                break
                            else:
                                number_3 += 1
                        self.dictionary[i] = number * number_2 // number_3
                        eval(f'self.text_{i}.setText("{number} * '
                             f'{number_2} ÷ {number_3} = ")')
        if self.flag == '6':
            for i in range(1, 21):
                eval(f'self.answer_{i}.setValidator(QIntValidator())')
                number = random.randint(2, 10)
                number_2 = random.randint(2, 10)
                self.dictionary[i] = number_2 * number
                eval(f'self.text_{i}.setText("{number} * {number_2}'
                         f'= ")')
        self.done.clicked.connect(self.check)

    def adds(self):
        with sql.connect("db/db_2.db") as db:
            cur = db.cursor()
            if self.stop == 1:
                self.full = int(cur.execute("""SELECT full FROM date
                WHERE email = ?""", (self.email,)).fetchall()[0][0]) + 1
                self.perfect = int(cur.execute("""SELECT perfect FROM date
        WHERE email = ?""", (self.email,)).fetchall()[0][0]) + self.perfect
                cur.execute("""UPDATE date SET full=? WHERE email=?""",
                            (self.full, self.email,))
                cur.execute("""UPDATE date SET perfect=? WHERE email=?""",
                            (self.perfect, self.email,))
            db.commit()

    def check(self):
        if self.stop != 0:
            return 0
        self.stop += 1
        self.total = 0
        for i in range(1, 21):
            r = False
            eval(f'self.answer_{i}.setEnabled(False)')
            if eval(f'self.answer_{i}.text()') != \
                            str(self.dictionary[i]):
                self.total += 1
                r = True
            if r:
                ans = eval(f'self.answer_{i}.text()')
                if ans:
                    ans = '\u0336'.join(ans) + '\u0336' + ' ' + str(self.dictionary[i])
                else:
                    ans = 'Вы не ввели ответ'
                eval(f'self.answer_{i}.setText("{ans}")')
        self.number = 2
        number_3 = random.randint(0, 4)
        self.support = ['Вы умничка! Двигайтесь в том же направлении!!',
                        'Молодец! Двигайся в том же направлении :)',
                        'Ура, вы смогли дойти до цели!',
                        'Похоже, я вижу перед собой гения', 'Класс!']
        if self.total == 0 and self.stop == 1:
            self.done.setText('МОЛОДЕЦ!!')
            self.number = 1
            f = open("all.txt", 'a')
            f.write(self.support[number_3])
            f.close()
            self.w = Pictures(self.number)
            self.w.show()
            self.result.setText(self.support[number_3])
            self.perfect = 1
            self.adds()
        elif self.total > 0:
            self.done.setText('Упс!')
            f = open("all.txt", 'a')
            word = morph.parse('ошибка')[0].make_agree_with_number(self.total).word
            res = f'Ой, у вас всего лишь {self.total} {word}, в следующий раз все получится! Я в вас верю.'
            f.write(res)
            self.result.setText(res)
            self.adds()
            self.w = Pictures(self.number)
            self.w.show()
