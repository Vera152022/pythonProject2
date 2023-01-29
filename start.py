import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from launch import Ui_MainWindow_1
import go
import register


class Beginning(QMainWindow, Ui_MainWindow_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Yes.clicked.connect(self.run)
        self.No.clicked.connect(self.run_2)

    def run(self):
        self.w = go.LogInToTheSystem()
        self.w.setFixedSize(800, 600)
        self.w.show()
        self.close()

    def run_2(self):
        self.w2 = register.RegistrationInTheSystem()
        self.w2.setFixedSize(800, 600)
        self.w2.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Beginning()
    ex.setFixedSize(660, 400)
    ex.show()
    sys.exit(app.exec_())