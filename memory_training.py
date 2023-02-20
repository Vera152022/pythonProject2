from PyQt5.QtWidgets import QMainWindow, QInputDialog
from memoryLevel_design import Ui_MainWindow
import random


class MemoryTraining(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.words = list(map(lambda x: x[:-1], open('slovar.txt').readlines()))
        self.s = 0
        self.mistakes = 0
        random.shuffle(self.words)
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
            for i in range(5):
                if not self.kostyl(eval(f'self.lineEdit_{i + 1}.text()')) == self.words[i]:
                    ans = '\u0336'.join(eval(f'self.lineEdit_{i + 1}.text()')) + '\u0336' + ' ' + str(self.words[i])
                    if eval(f'self.lineEdit_{i + 1}.text()') == '':
                        eval(f'self.lineEdit_{i + 1}.setText("Нет ответа")')
                    else:
                        eval(f'self.lineEdit_{i + 1}.setText("{ans}")')
                    self.mistakes += 1
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
        elif self.s == -1:
            self.close()

    def kostyl(self, word):
        f = ''
        for e in list(word):
            if e == 'ё':
                f += 'е'
            else:
                f += e
        return f

