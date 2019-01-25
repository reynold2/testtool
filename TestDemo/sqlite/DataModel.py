
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
import sys
import time
class SqlModel(object):
    def __init__(self,databasetype="QSQLITE",databasename="data.db",sqltablename="里程碑"):
        db=QSqlDatabase.addDatabase(databasetype)
        db.setDatabaseName(databasename)
        self.sqltablename=sqltablename
        self.__tablemodel()
    def __tablemodel(self):
        self.model=QSqlTableModel()
        self.model.setTable(self.sqltablename)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
    def modelview(self):
        self.view=QTableView()
        self.view.setModel(self.model)
        # modelwidget=QTabWidget()
        # modelwidget.addTab(self.view, viewname)
        return self.view
    def tabadd(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row)
        self.view.setCurrentIndex(index)
        self.view.edit(index)
    def tabdel(self):
        index = self.modelview().currentIndex()
        print(index)
        # self.model.removeRow(index.row())
    def tabupdate(self):

        self.model.updateRowInTable()
    def row(self):
        row=self.model.rowCount()
        return row
    def line(self):
        line=self.model.columnCount()
        return line
    def rowvalue(self):
        rowvalue=self.model.insertRowIntoTable(QSqlRecord="")
    def data(self):
        self.model.data()
    def run(self,WindowTitle= "data"):
        app = QApplication(sys.argv)
        dig=QDialog()
        layout=QHBoxLayout()
        layout.addWidget(self.modelview())
        dig.setLayout(layout)
        dig.setWindowTitle(WindowTitle)
        dig.resize(430,450)
        # dig.hide()
        # time.sleep(10)
        dig.show()
        sys.exit(app.exec_())


if __name__=="__main__":
    m=SqlModel()

    m.run()


