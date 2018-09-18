from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
import sys
import time
# app = QApplication([])
#
#
# class PopupView(QWidget):
#     def __init__(self, parent=None):
#         super(PopupView, self).__init__(parent)
#         self.setWindowFlags(Qt.Popup)
#         self.move(QCursor.pos())
#         self.show()
#
#
# class ItemDelegate(QItemDelegate):
#     def __init__(self, parent):
#         QItemDelegate.__init__(self, parent)
#
#     def createEditor(self, parent, option, index):
#         return PopupView(parent)
#
#
# class Model(QAbstractTableModel):
#     def __init__(self):
#         QAbstractTableModel.__init__(self)
#         self.items = [[1, 'one', 'ONE'], [2, 'two', 'TWO'], [3, 'three', 'THREE']]
#
#     def flags(self, index):
#         return Qt.ItemIsEnabled | Qt.ItemIsEditable
#
#     def rowCount(self, parent=QModelIndex()):
#         return 3
#
#     def columnCount(self, parent=QModelIndex()):
#         return 3
#
#     def data(self, index, role):
#         if not index.isValid():
#             return
#
#         if role in [Qt.DisplayRole, Qt.EditRole]:
#             return self.items[index.row()][index.column()]
#
#
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self, parent)
#         self.clipboard = QApplication.clipboard()
#         mainWidget = QWidget()
#         self.setCentralWidget(mainWidget)
#         mainWidget.setLayout(QVBoxLayout())
#
#         view = QTableView()
#         view.setModel(Model())
#         view.setItemDelegate(ItemDelegate(view))
#         self.layout().addWidget(view)
#
#
# view = MainWindow()
# view.show()
# app.exec_()
app=QApplication(sys.argv)
db=QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("data.db")

model=QSqlTableModel()

model.setTable("Feature")

model.setEditStrategy(QSqlTableModel.OnFieldChange)
model.select()
model.setHeaderData(0,Qt.Horizontal,"序号")
model.setHeaderData(1,Qt.Horizontal,"功能点")
model.setHeaderData(2,Qt.Horizontal,"里程碑1")
model1=QSqlTableModel()
model1.setTable("版本")
model1.select()
view=QTableView()
view.setModel(model)

view1=QTableView()
view1.setModel(model1)


w=QTabWidget()
w.addTab(view,"tate")
w.addTab(view1,"ttt")
dig=QDialog()

layout=QHBoxLayout()
layout.addWidget(w)

dig.setLayout(layout)
dig.setWindowTitle("data")
dig.resize(430,450)
# dig.hide()
# time.sleep(10)
dig.show()
sys.exit(app.exec_())




