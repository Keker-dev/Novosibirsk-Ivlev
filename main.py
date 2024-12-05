import sys
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6 import uic
import io

with open("main.ui", "r", encoding="utf8") as f:
    TEMPLATE = f.read()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(TEMPLATE), self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('Coffee')
        model.select()

        self.view.setModel(model)
        self.view.move(10, 10)
        self.view.resize(780, 580)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
