'''
Created on 2018年7月6日

@author: Administrator
'''
from PyQt5.QtWidgets import QTableWidget, QHBoxLayout, QWidget, QAbstractItemView, QHeaderView, QPushButton, QTableWidgetItem, QComboBox, QApplication

from PyQt5.QtCore import QAbstractTableModel
from DataManger import MangerData
from Gvariable import *
import sys


class CentralView(QTableWidget):

    def __init__(self):
        super(CentralView, self).__init__()
        self.temp = ()
        self.idlist = []
        self.datalist = []
        self.templist = []
        self.table_widget = QTableWidget()
        self.ExcleView()
        self.ExtensionButton()
        self.table_widget.removeRow(0)
        hhbox = QHBoxLayout()
        hhbox.addWidget(self.table_widget)  # 把表格加入布局
        self.setLayout(hhbox)
#         self.table()
        self.compose_id()

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
        for i in range(self.row):
            self.idlist.append(
                self.table_widget.item(i, 0).text())
        del self.idlist[0]
        self.templist.extend(self.exdatalist)
        return self.idlist

    def buttonForRow(self, id):
        widget = QWidget()
        PreviewsBtn = QPushButton('预览')
        PreviewsBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

        PreviewsBtn.clicked.connect(self.Previews)
        backBtn = QPushButton('回放')

        backBtn.setStyleSheet(''' text-align : center;
                                  background-color : DarkSeaGreen;
                                  height : 30px;
                                  border-style: outset;
                                  font : 13px; ''')
        backBtn.clicked.connect(self.Previews)
        screenshotBtn = QPushButton('截图')
        screenshotBtn.setStyleSheet(''' text-align : center;
                                   background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                   font : 13px; ''')
        screenshotBtn.clicked.connect(self.Previews)
        hLayout = QHBoxLayout()
        hLayout.addWidget(PreviewsBtn)
        hLayout.addWidget(backBtn)
        hLayout.addWidget(screenshotBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def Previews(self, x):
        send = self.sender()
#         send.parent_name
        print(send.pos())
        for idx in self.tempid:
            for x in idx:

                print(id(x))

    def compose_id(self):
        self.idlist
#         for id in self.idlist:
#             print(id)
#         for idx in self.tempid:
#             print(idx)

    def table(self):
        #         row = self.table_widget.rowCount()
        #         for x in range(row):
        #             print(x)
        self.table_widget.item

    def ExtensionButton(self):
        self.Defaultlistdata = []
        self.tempid = []
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
            self.tempid.append(self.buttonForRow(id).children())
            self.combox.currentTextChanged.connect(self.onActivated)
        return self.Defaultlistdata

    def onActivated(self, x):
        self.listobjx = []
        send = self.sender()
        self.duixiang[send] = x
        xlist = list(self.duixiang.values())

        for i in range(self.row):
            if i == 0:
                pass
            else:
                self.listobjx.append(i)
                self.listobjx.append(self.colum)
                self.listobjx.append(xlist[i])

        self.temp = tuple(self.listobjx)

        self.datalist = self.templist + list(self.temp)
        return self.datalist

    def save_table(self,path):
        s = MangerData()
        s.SetExcel(location=path,
            datalist=self.datalist)


class MyModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        list1 = []
        list2 = []
        print("tab", id(PATHDATA))
        dizhi = PATHDATA["case"]
        self.data = MangerData().GetExcel(location=dizhi)
        if self.data == None:
            self.data = ["1", "1", ""]
        else:
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
