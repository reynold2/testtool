'''
Created on 2018年7月6日

@author: Administrator
'''
from PyQt5.QtWidgets import QTableWidget, QHBoxLayout, QWidget, QAbstractItemView, QHeaderView, QPushButton, \
    QTableWidgetItem, QComboBox, QApplication, QMessageBox

from PyQt5 import QtWidgets
from PyQt5.QtCore import QAbstractTableModel,Qt,pyqtSignal
from tool.DataManger import MangerData
from tool.Gvariable import *
from PyQt5.QtGui import QIcon
import re
import sys
from tool.CaseData import CaseData
from tool.ImageComparison import Photoshop
from tool.ProcessCalls import Runexe
import time
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class CentralView(QTableWidget):
    cunt = 0
    def __init__(self):
        super(CentralView, self).__init__()
        self.id=None
        self.updatetemp={}
        self.reportdict={}
        self.updatetemp1={}
        self.idlist = []
        self.datalist = []
        self.templist = []
        self.table_widget = QTableWidget()
        self.ExcleView()
        self.ExtensionButton()
        self.table_widget.removeRow(0)
        self.shortcut_init()
        hhbox = QHBoxLayout()
        tab = QtWidgets.QTabWidget()
        tab.addTab(self.table_widget, QIcon("res/open.png"), "测试用例")
        hhbox.addWidget(tab)
        self.setLayout(hhbox)

    def shortcut_init(self):
        self.shortcut = QShortcut(QKeySequence("Ctrl+h"), self)
        self.shortcut.activated.connect(self.shortcutprintscreen)
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
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.setMouseTracking(True)
        self.table_widget.setStyleSheet("selection-background-color:red")
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
        self.datalist = self.templist

        return self.idlist


    def buttonForRow(self):

        widget = QWidget()
        RunBtn = QPushButton('运行')
        RunBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

        RunBtn.clicked.connect(self.SingleRun)
        ScreenBtn = QPushButton('截图')
        ScreenBtn.setStyleSheet(''' text-align : center;
                                  background-color : DarkSeaGreen;
                                  height : 30px;
                                  border-style: outset;
                                  font : 13px; ''')
        ScreenBtn.clicked.connect(self.printscreen)
        LocationScreenBtn = QPushButton("条件截图",self)
        LocationScreenBtn.setShortcut('Ctrl+L')
        LocationScreenBtn.setStyleSheet(''' text-align : center;
                                   background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                   font : 13px; ''')
        LocationScreenBtn.clicked.connect(self.shortcutprintscreen)
        hLayout = QHBoxLayout()

        hLayout.addWidget(ScreenBtn)
        hLayout.addWidget(RunBtn)
        hLayout.addWidget(LocationScreenBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)

        return widget

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_L:
    #         self.shortcutpng.emit()

    def __translate(self, send,n):
        keyvalue = {}
        list1 = []
        for index, x in enumerate(self.tempid):
            z = re.split(r", ", x)
            list1.append(z[n])
        del list1[-1]
        Z = dict(zip(list1, self.idlist))

        return Z

    def SingleRun(self):
        try:
            _id = set(self.idlist)
            _casedata=CaseData("res/RE")
            _dir =_casedata._dirset()
            extension=_casedata.key_value()[1]
            report = _casedata.key_value()[2]
            _cha = _id - (_id & _dir)
            if CentralView.cunt == 0:
                if _cha:
                    reply = QMessageBox.warning(self, '当前路径下缺失用例名称为:%s' % _cha.pop(),
                                                "当前测试用例数据不完整将无法批量执行是否不再提示?", QMessageBox.Yes |
                                                QMessageBox.No, QMessageBox.No)

                    if reply == QMessageBox.Yes:
                        CentralView.cunt = 1
                    else:
                        CentralView.cunt = 0
                else:
                    pass
            else:
                pass
            send = self.sender()
            run_idcase = self.__translate(send,2).get(str(send), str(send))
            if str(send) == run_idcase:
                print("当前是异常数据项:%s" % run_idcase)
            else:
                PS=Photoshop(PATHDATA.get("data"))
                time.sleep(0.5)
                self.exe = Runexe(run_idcase)
                self.exe.start()
                time.sleep(3)
                print(report.get(run_idcase))
                if report.get(run_idcase)is None:
                    print(report.get(run_idcase))
                else:
                    PS.grab(report.get(run_idcase))
                RT=PS.alignment_section(extension.get(run_idcase),report.get(run_idcase))
                if RT:
                    self.reportdict[run_idcase] = "通过"
                else:
                    self.reportdict[run_idcase] = "不通过"
                # print(self.reportdict)
            self.id=run_idcase
            self.shortcutpng.connect(self.shortcutprintscreen)
            return self.id
        except:
            print("数据无效无法启动")
        finally:

            listi=[]

            for x in self.idlist:
                self.updatetemp[x][2]=self.reportdict[x]
                listi=listi+self.updatetemp[x]
            self.datalist=self.templist + listi



    def printscreen(self):
        try:
            send = self.sender()
            extension_idcase1 = self.__translate(send, 3).get((str(send) + "]"), str(send))
            if extension_idcase1 == str(send):
                print("当前是异常数据项:%s" % extension_idcase1)
            else:
                _casedata = CaseData(PATHDATA.get("data"))
                extension = _casedata.key_value()[1]
                self.PS = Photoshop(PATHDATA.get("data"))
                self.PS.grab(extension.get(extension_idcase1))
                print("截图完毕，路径下已存在：%s" % extension.get(extension_idcase1))
        except:
            print("无法截图")
    @pyqtSlot()
    def shortcutprintscreen(self):
        try:
            if type(self.id)is str:
                print("正在使用快捷键对运行程序截图：名称为%s的测试用例"%self.id)
                self.PS = Photoshop(PATHDATA.get("data"))
                print("%s/%s.extension.png"%(PATHDATA.get("data"),self.id))
                self.PS.grab("%s/%s.extension.png"%(PATHDATA.get("data"),self.id))
        except:
            print("目标未启动无法截图")
        # if self.table_widget.selectedItems()
        # print(self.table_widget.selectedItems()[0].text())

        # print(self.table_widget.itemClicked(self.table_widget.currentItem()))
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
            self.reportdict[self.idlist[i - 1]] = "通过"
            self.updatetemp[self.idlist[i - 1]] = [i, self.colum, "通过"]


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
                self.updatetemp[self.idlist[i - 1]] = [i, self.colum, xlist[i]]
        self.temp = tuple(self.listobjx)
        self.datalist = self.templist + self.listobjx
        return self.datalist
    def idr(self):
        if hasattr(self,"listobjx"):
            self.datalist = self.templist + self.listobjx
            for x in self.idlist:
                self.updatetemp[x][2]=self.reportdict[x]

    def save_table(self, path):
        print(path)
        try:
            s = MangerData()
            s.SetExcel(location=path, datalist=self.datalist)
        except:
            print("数据异常无法保存")

class MyModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        list1 = []
        list2 = []
        dizhi = PATHDATA["case"]
        self.data = MangerData().GetExcel(location=dizhi)
        if self.data is None:
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
