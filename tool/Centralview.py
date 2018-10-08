'''
Created on 2018年7月6日

@author: Administrator
'''
from PyQt5.QtWidgets import QTableWidget, QHBoxLayout, QWidget, QAbstractItemView, QHeaderView, QPushButton, \
    QTableWidgetItem, QComboBox, QApplication

from PyQt5.QtCore import QAbstractTableModel
from tool.DataManger import MangerData
from tool.Gvariable import *
import re
import sys
from  tool.ProcessCalls import Runexe
import time
from sqlite.DataModel import SqlModel
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
    #         self.compose_id()

    def ExcleView(self):

        self.exdatalist = []
        model = SqlModel()
        self.data = model.model.data()
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
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
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

    def buttonForRow(self):

        widget = QWidget()
        PreviewsBtn = QPushButton('运行')
        PreviewsBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

        PreviewsBtn.clicked.connect(self.Previews)
        backBtn = QPushButton('截图')
        backBtn.setStyleSheet(''' text-align : center;
                                  background-color : DarkSeaGreen;
                                  height : 30px;
                                  border-style: outset;
                                  font : 13px; ''')
        backBtn.clicked.connect(self.compose_id)
        screenshotBtn = QPushButton('注')

        screenshotBtn.setStyleSheet(''' text-align : center;
                                   background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                   font : 13px; ''')
        screenshotBtn.clicked.connect(self.png)
        hLayout = QHBoxLayout()
        hLayout.addWidget(PreviewsBtn)
        hLayout.addWidget(backBtn)
        hLayout.addWidget(screenshotBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def __translate(self):
        list1 = []
        for x in self.tempid:
            # list1.append(x[105:155])
            z = re.split(r", ", x)
            list1.append(z[2])
        del list1[-1]
        Z = dict(zip(list1, self.idlist))
        return Z
    def Previews(self):
        send = self.sender()
        print(self.__tranrunslate())
        x = self.__tranrunslate()[str(send)]
        time.sleep(0.5)
        self.run = Runexe(x)
        self.run.start()
        time.sleep(0.5)
        # return x

    def compose_id(self):
        send = self.sender()
        print(send)

    def table(self):

        self.table_widget.item

    def png(self):
        send = self.sender()
        print(send)

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
                i, self.colum + 1, self.buttonForRow())
            # self.tempid.append(self.buttonForRow().children())
            self.tempid.append(self.buttonForRow().children().__repr__())
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

    def save_table(self, path):
        s = MangerData()
        s.SetExcel(location=path, datalist=self.datalist)


# class MyModel(QAbstractTableModel):
#     def __init__(self):
#         super().__init__()
#         list1 = []
#         list2 = []
#         dizhi = PATHDATA["case"]
#         self.data = MangerData().GetExcel(location=dizhi)
#         if self.data is None:
#             self.data = ["1", "1", ""]
#         else:
#             for i in range(0, len(self.data), 3):
#                 b = self.data[i:i + 3]
#                 list1.append(b[0])
#                 list2.append(b[1])
#             self.rownew = max(list1) + 1
#             self.columnew = max(list2) + 1
#
#     def row(self):
#         return self.rownew
#
#     def colum(self):
#         return self.columnew
#
#     def data(self):
#         return self.data


if __name__ == '__main__':
    a = QApplication(sys.argv)
    tableView = CentralView()

    tableView.show()

    a.exec_()
