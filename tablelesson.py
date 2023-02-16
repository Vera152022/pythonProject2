from PyQt5.QtWidgets import QMainWindow, QInputDialog
from table_design import Ui_MainWindow
import random
import datetime as dt
from pictere_2 import Pictures


class TableLesson(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.start)
        self.st = None

    def start(self):
        self.label.hide()
        self.startButton.hide()
        r = list(range(1, 26))
        random.shuffle(r)
        for i in range(25):
            eval(f'self.B{i + 1}.setText("{r[i]}")')

