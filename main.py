import sys
import sqlite3
import class_main
import class_second_form
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6 import uic


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow, class_main.Ui_MainWindow):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.name = name

        self.show_table()
        self.addButton.clicked.connect(self.open_sec_form)

    def show_table(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(self.name)
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('Coffee')
        model.select()

        self.view.setModel(model)
        self.view.move(10, 10)
        self.view.resize(780, 580)

    def open_sec_form(self):
        self.SecForm = SecondForm(self, self.show_table, 'coffee.sqlite')
        self.SecForm.show()


class SecondForm(QWidget, class_second_form.Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.name = args[-1]
        self.OKButton.clicked.connect(self.add_value)
        self.OKButton.clicked.connect(args[-2])
        self.OKButton.clicked.connect(self.close)

    def add_value(self):
        con = sqlite3.connect(self.name)
        cur = con.cursor()
        mx_id = max(map(lambda a: a[0], cur.execute("SELECT id from Coffee").fetchall())) + 1
        brand = self.VarEdit.text()
        roast = self.RoastEdit.text()
        beans = self.BeansEdit.text()
        desc = self.DescEdit.text()
        coast = self.CoastEdit.text()
        mass = self.MassEdit.text()
        if coast.isdigit() and mass.isdigit():
            coast, mass = int(coast), int(mass)
        else:
            coast, mass = 0, 0
        params = (mx_id, brand, roast, beans, desc, coast, mass)
        cur.execute(f"""INSERT INTO Coffee(ID, varietie, roast, beans, describe, coast, mass) VALUES {params}""")
        con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example('data\\coffee.sqlite')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
