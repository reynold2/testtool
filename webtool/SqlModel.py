# -*- coding: UTF-8 -*-
#！usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlRelationalTableModel,QSqlRelation
from PyQt5.Qt import Qt,QTimer,QCoreApplication
from webtool.threads import RunThread
from webtool.log_config import LOGER
import time
import sys

class Model_View(object):
    def __init__(self,databasetype="QSQLITE",databasename="sql/testcase.db",sqltablename="result"):
        db=QSqlDatabase.addDatabase(databasetype)
        db.setDatabaseName(databasename)
        self.sqltablename=sqltablename
        self.__tablemodel()
    def __tablemodel(self):
        # self.model=QSqlTableModel()
        # self.model.setRelation(4,QSqlRelation("TEST","id_test","method_name"))
        self.model=QSqlRelationalTableModel()
        self.model.setTable(self.sqltablename)
        self.model.setHeaderData(0, Qt.Horizontal, '用例ID')
        self.model.setHeaderData(1, Qt.Horizontal, '用例名称')
        self.model.setHeaderData(2, Qt.Horizontal, '脚本名称')
        self.model.setHeaderData(3, Qt.Horizontal, '执行状态')
        self.model.setHeaderData(4, Qt.Horizontal, '结论')
        self.model.setHeaderData(5, Qt.Horizontal, '时间')
        self.model.setHeaderData(6, Qt.Horizontal, '操作')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
    #讲所有测试用例的
    def modelview(self):
        self.view=QTableView()
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.view.setModel(self.model)
        for index in range(self.model.rowCount()):
            case_name=self.model.data(self.model.index(index, 2))
            self.view.setIndexWidget(self.model.index(index, 6), self.button(case_name))
            # self.view.setIndexWidget(self.model.index(index, 5), self.time(case_name))
        return self.view
    def button(self,id):
        widget = QWidget()
        Btn = QPushButton('执行')
        Btn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 15px  ''')

        Btn.clicked.connect(lambda: self.Work(id))
        self.timer = QTimer()
        # self.timer.timeout.connect(self.CountTime)
        hLayout = QHBoxLayout()
        hLayout.addWidget(Btn)
        hLayout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(hLayout)
        return widget
    # def time(self,case_name):
    #
    #     return QLCDNumber()

    # def CountTime(self):
    #     self.t += 1
    #     self.time(self.name).display(self.t)
    def Work(self,index):
        self.name=index
        self.timer.start(1000)
        self.thread = RunThread(index)
        self.thread.start()
        self.thread.thread_signal.connect(self.TimeStop)
    # @staticmethod
    # def allrun():
    #
    #     thread = RunThread(0)
    #     thread.start()
    #     # thread.join()
    #     QCoreApplication.processEvents()
    def TimeStop(self):
        self.timer.stop()
        LOGER.loginfo(self.name+"用例执行完毕，邮件已发送")
        print("用例运行完毕，邮件已发送")



if __name__=="__main__":
    m=Model_View()
    app = QApplication(sys.argv)
    dig=QDialog()
    layout=QHBoxLayout()
    layout.addWidget(m.modelview())
    dig.setLayout(layout)
    dig.setWindowTitle("test")
    dig.resize(800,400)
    dig.show()
    sys.exit(app.exec_())

