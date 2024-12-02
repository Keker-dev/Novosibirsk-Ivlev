import sys
from random import randint as rd
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton


class MainWind(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Рисование')
        self.CreateButton = QPushButton("Создать круг", self)
        self.CreateButton.resize(221, 51)
        self.CreateButton.move(290, 10)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(MainWind):
    def __init__(self):
        super().__init__()
        self.CreateButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        color = QColor(rd(0, 255), rd(0, 255), rd(0, 255))
        size = rd(10, 150)
        qp.setBrush(color)
        qp.drawEllipse(QPoint(400, 300), size, size)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
