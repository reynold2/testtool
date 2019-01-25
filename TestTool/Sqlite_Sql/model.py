#coding=utf-8
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlRelationalTableModel
from PyQt5.Qt import Qt

class Model(object):
    def __init__(self,databasetype="QSQLITE",databasename="Sqlite_Sql/testcase.db",sqltablename="result"):
        db=QSqlDatabase.addDatabase(databasetype)
        db.setDatabaseName(databasename)
        self.sqltablename=sqltablename
        self.tablemodel()
    def tablemodel(self):
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

