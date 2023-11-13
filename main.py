from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import uic
import random
from UI import Ui_Form


class App(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.circle)
        self.draw = False

    def circle(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, pe) -> None:
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            d = random.randint(1, min(self.width(), self.height()))
            rect = QRect(random.randint(0, self.width() - d, random.randint(0, self.height() - d), d, d))
            qp.setBrush(QColor('Yellow'))
            qp.drawEllipse(rect)
            qp.end()
            self.draw = False


def exept_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.excepthook = exept_hook
    sys.exit(app.exec())
