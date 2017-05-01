from form import Ui_Form
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog
from PyQt5.QtCore import QThread
import pymongo, json

conn = pymongo.MongoClient('localhost', 27017)
conn_db = conn['example']
coll = conn_db['setdata']
count = coll.count()
data = coll.find()

class MainWindowSlots(Ui_Form):
    def writeToTable(self):
        self.tableWidget.setRowCount(count)
        for val, i in zip(data, range(count)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(val['_id'])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(val['author']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(val['title']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(val['url']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(val['text']))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(val['price']))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(val['currency']))
        return None

    def save_file(self):
        filename = QFileDialog.getSaveFileName()
        file = open(filename[0], 'a')
        for i in data:
            json.dump(str(i), file)
        file.close()