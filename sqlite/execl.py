import xlrd

class x(object):
    def __init__(self,path="TestData1.xls"):
        self.path=path
    def read_excel(self):
        list=[]
        workbook = xlrd.open_workbook(self.path)
        sheet_name = workbook.sheet_names()[0]
        sheet = workbook.sheet_by_name(sheet_name)
        for x in range(sheet.nrows):
            # list.append(tuple(map(lambda x:x.encode("utf-8"),sheet.row_values(x))))
            list.append(tuple(sheet.row_values(x)))
        return list


import sys
from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex, QVariant)
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QItemDelegate, QPushButton, QTableView, QWidget)


class MyModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(MyModel, self).__init__(parent)

    def rowCount(self, QModelIndex):
        return 4

    def columnCount(self, QModelIndex):
        return 3

    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return 'Row %d, Column %d' % (row + 1, col + 1)
        return QVariant()


# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("各个市场比特币实时行情")  # 设置表格名称
        self.setWindowIcon(QIcon("ok.png"))  # 设置图标（图片要存在）
        self.resize(600, 200)  # 设置表格尺寸（整体大小）
        self.setColumnCount(5)  # 设置列数
        self.setRowCount(5)  # 设置行数
        # self.setColumnWidth(0, 200)  # 设置列宽(第几列， 宽度)
        # self.setRowHeight(0, 100)  # 设置行高(第几行， 行高)

        column_name = [
            'ETH/BIC',
            'column1',
            'column2',
            'column3',
            'column4',
        ]
        self.setHorizontalHeaderLabels(column_name)  # 设置列名称
        row_name = [
            'binance',
            'okex',
            'bitfinex',
            'bittrex',
            'bithumb',
        ]
        self.setVerticalHeaderLabels(row_name)  # 设置行名称

    def update_item_data(self, data):
        """更新内容"""
        self.setItem(0, 0, QTableWidgetItem(data))  # 设置表格内容(行， 列) 文字


class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            self.update_date.emit(str(cnt))  # 发射信号
            time.sleep(1)


if __name__ == '__main__':
    # 实例化表格
    app = QApplication(sys.argv)
    myTable = MyTable()
    # 启动更新线程
    update_data_thread = UpdateData()
    update_data_thread.update_date.connect(myTable.update_item_data)  # 链接信号
    update_data_thread.start()

    # 显示在屏幕中央
    desktop = QApplication.desktop()  # 获取坐标
    x = (desktop.width() - myTable.width()) // 2
    y = (desktop.height() - myTable.height()) // 2
    myTable.move(x, y)  # 移动

    # 显示表格
    myTable.show()
    app.exit(app.exec_())




