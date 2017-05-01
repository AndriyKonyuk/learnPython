"""
Пользовательские слоты для виджетов.
"""

from form import Ui_Form
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog
from PyQt5.QtCore import QThread
import pymongo, json


# Создаём собственный класс, наследуясь от автоматически сгенерированного
class MainWindowSlots(Ui_Form):
    # Определяем пользовательский слот
    def writeToTable(self):
        self.conn_to_db()
        for val, i in zip(self.data, range(self.count)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(val['_id'])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(val['author']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(val['title']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(val['url']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(val['text']))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(val['price']))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(val['currency']))

        widget = super().tableWidget
        widget.setItem(widget.setRowCount(self.count))
        return None

    def conn_to_db(self):
        conn = pymongo.MongoClient('localhost', 27017)
        conn_db = conn['example']
        coll = conn_db['setdata']
        self.count = coll.count()
        self.data = coll.find()

    def save_file(self):
        self.conn_to_db()
        filename = QFileDialog.getSaveFileName()
        file = open(filename[0], 'a')
        for i in self.data:
            json.dump(str(i), file)
        file.close()