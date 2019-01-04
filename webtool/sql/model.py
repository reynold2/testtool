#coding=utf-8
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlRelationalTableModel,QSqlRelation
from PyQt5.Qt import Qt

class Model(object):
    def __init__(self,databasetype="QSQLITE",databasename="testcase.db",sqltablename="result"):
        db=QSqlDatabase.addDatabase(databasetype)
        db.setDatabaseName(databasename)
        self.sqltablename=sqltablename
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

    # def tabadd(self):
    #     row = self.model.rowCount()
    #     self.model.insertRow(row)
    #     index = self.model.index(row)
    #     self.view.setCurrentIndex(index)
    #     self.view.edit(index)
    # def tabdel(self):
    #     index = self.modelview().currentIndex()
    #     # self.model.removeRow(index.row())
    # def tabupdate(self):
    #     self.model.updateRowInTable()
    # def row(self):
    #     row=self.model.rowCount()
    #     return row
    # def line(self):
    #     line=self.model.columnCount()
    #     return line
    # def rowvalue(self):
    #     rowvalue=self.model.insertRowIntoTable(QSqlRecord="")
    # def data(self):
    #     self.model.data()
