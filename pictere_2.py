from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow


class Pictures(QMainWindow):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.initUI()

    def initUI(self):
        if self.number == 1:
            self.setGeometry(630, 200, 670, 320)
            self.setFixedSize(670, 320)
            self.pixmap = QPixmap('thanks.jpg')
            self.image = QLabel(self)
            self.image.move(10, 10)
            self.image.resize(700, 480)
            self.image.setPixmap(self.pixmap)
        elif self.number == 2:
            self.setGeometry(700, 150, 544, 434)
            self.setFixedSize(544, 434)
            self.pixmap = QPixmap('picture_2.jpeg')
            self.image = QLabel(self)
            self.image.move(10, 10)
            self.image.resize(700, 540)
            self.image.setPixmap(self.pixmap)
        elif self.number == 3:
            self.setGeometry(700, 150, 425, 320)
            self.setFixedSize(425, 320)
            self.pixmap = QPixmap('picture_4.jpg')
            self.image = QLabel(self)
            self.image.move(10, 10)
            self.image.resize(400, 300)
            self.image.setPixmap(self.pixmap)
        elif self.number == 4:
            self.setGeometry(700, 150, 420, 340)
            self.setFixedSize(420, 340)
            self.pixmap = QPixmap('picture_5.jpg')
            self.image = QLabel(self)
            self.image.move(10, 10)
            self.image.resize(400, 320)
            self.image.setPixmap(self.pixmap)