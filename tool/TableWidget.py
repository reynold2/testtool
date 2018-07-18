'''
Created on 2018年7月6日

@author: Administrator
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DataManger import MangerData
from DataIo import excel_io
import sys
from PyQt5 import QtCore


class CentralView(QTableWidget):

    def __init__(self, datalist=[]):
        super(CentralView, self).__init__()
        self.datalist = []
        self.table_widget = QTableWidget()
        self.ExcleView()
        self.ExtensionButton()
        self.table_widget.removeRow(0)
#         self.data = MangerData().GetExcel()

#         self.table_widget.removeRow(self.colum)


#         self.table_widget.setColumnWidth(0, 40)
        hhbox = QHBoxLayout()
        hhbox.addWidget(self.table_widget)  # 把表格加入布局
        self.setLayout(hhbox)

    def ExcleView(self):

        self.exdatalist = []
        model = MyModel()
        self.data = model.data
        self.exdatalist = self.data
        self.row = model.row()
        self.colum = model.colum()

        self.table_widget.setRowCount(self.row + 1)
        self.table_widget.setColumnCount(self.colum + 2)
        self.table_widget.setHorizontalHeaderLabels(
            ["用例编号", "用例标题", "用例步骤", "期望结果", "测试人员", "备注", "状态", "附件"])
#         self.table_widget.setVerticalHeaderLabels(
#             ["用例编号", "用例标题", "用例步骤", "期望结果"])
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setEditTriggers((QAbstractItemView.NoEditTriggers))
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.removeRow(self.row - 1)

        for i in range(0, len(self.data), 3):
            b = self.data[i:i + 3]
            self.table_widget.setItem(b[0], b[1],
                                      QTableWidgetItem(b[2]))

        self.datalist.extend(self.exdatalist)

    def buttonForRow(self, id):
        widget = QWidget()
        updateBtn = QPushButton('预览')
        updateBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

#         updateBtn.clicked.connect(lambda: self.updateTable(id))
        viewBtn = QPushButton('回放')
        viewBtn.setStyleSheet(''' text-align : center;
                                  background-color : DarkSeaGreen;
                                  height : 30px;
                                  border-style: outset;
                                  font : 13px; ''')
#         viewBtn.clicked.connect(lambda: self.viewTable(id))
        deleteBtn = QPushButton('截图')
        deleteBtn.setStyleSheet(''' text-align : center;
                                   background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                   font : 13px; ''')
#         viewBtn.clicked.connect(lambda: self.viewTable(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def ExtensionButton(self):
        self.Defaultlistdata = []
        self.duixiang = {}
        for i in range(self.row):
            self.combox = QComboBox()
            self.combox.addItems(["通过", "不通过"])
            self.Defaultlistdata.append(i)
            self.Defaultlistdata.append(self.colum)
            self.Defaultlistdata.append("通过")
            self.combox.setStyleSheet(''' text-align : center;
                                   background-color : green;
                                    height : 30px;
                                    border-style: outset;
                                   font : 13px; ''')

            self.table_widget.setCellWidget(i, self.colum, self.combox)
            self.duixiang[self.combox] = "通过"

            self.table_widget.setCellWidget(
                i, self.colum + 1, self.buttonForRow(id))
            self.combox.currentTextChanged.connect(self.onActivated)
        return self.Defaultlistdata

    def onActivated(self, x):
        self.listobjx = []
        send = self.sender()
        self.duixiang[send] = x
        xlist = list(self.duixiang.values())
        for i in range(self.row):
            self.listobjx.append(i)
            self.listobjx.append(self.colum)
            self.listobjx.append(xlist[i])
        self.datalist.extend(self.listobjx)
        return self.datalist

    def freshen(self, path):

        return self.table_widget.show()

    def save_table(self):
        s = MangerData()
        s.SetExcel(ischangecontent=True,
                   loc="G:/Python3/layout/tool/RE/report.xls", listdata=self.datalist)


class MyModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        list1 = []
        list2 = []
        self.data = MangerData().GetExcel()
        for i in range(0, len(self.data), 3):
            b = self.data[i:i + 3]
            list1.append(b[0])
            list2.append(b[1])
        self.rownew = max(list1) + 1
        self.columnew = max(list2) + 1

    def row(self):
        return self.rownew

    def colum(self):
        return self.columnew

    def data(self):
        return self.data


if __name__ == '__main__':
    a = QApplication(sys.argv)
    tableView = CentralView()

    tableView.show()
    a.exec_()
