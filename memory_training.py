from PyQt5.QtWidgets import QMainWindow, QInputDialog
from memoryLevel_design import Ui_MainWindow
import random
import datetime as dt
from pictere_2 import Pictures


class MemoryTraining(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.words = list(map(lambda x: x[:-1], open('slovar.txt').readlines()))

    def start(self):
        random.shuffle(self.words)
        for i in range(5):
            eval(f'self.label_{i + 1}.setText("{self.words[i]}")')
