import sys
from random import randint as rd
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import io

with open("UI.ui", "r", encoding="utf8") as f:
    TEMPLATE = f.read()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(TEMPLATE), self)
        self.CreateButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        size = rd(10, 150)
        qp.drawEllipse(QPoint(400, 300), size, size)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
