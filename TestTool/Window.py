# -*- coding: UTF-8 -*-
#！usr/bin/python
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QMenuBar,QTabBar,QAction
from PyQt5.QtGui import QIcon
import sys
from TestTool.SqlModel import Model_View
class UI(QMainWindow):
    def __init__(self, parent=None):
        super(UI,self).__init__(parent)
        self.central_view = Model_View()
        self.central_widget = self.central_view.modelview()
        self.__window__()
    def __window__(self):
        self.__menuBar()
        self.__toolbar()
        self.__dockview()
        self.setGeometry(100, 100, 1120, 750)
        self.setWindowTitle("Test")
        self.setCentralWidget(self.central_widget)
        self.show()
    def __menuBar(self):
        menus=QMenuBar()
    def __toolbar(self):
        runbutton = QAction(QIcon("Res/save.png"), "测试", self)
        runbutton.setShortcut("ctrl+R")
        runbutton.setStatusTip("一件操作")

        openreport = QAction(QIcon("Res/save.png"), "打开报告", self)
        openreport.setShortcut("ctrl+p")
        openreport.setStatusTip("报告")

        tb = self.addToolBar("工具栏")
        tb.addAction(runbutton)
        tb.addAction(openreport)

        runbutton.triggered.connect(self.mianrun)
        openreport.triggered.connect(self.openreport)

    def __dockview(self):
        pass
    def __centerview(self):
        pass
    def mianrun(self):
        self.central_view.Work("test_baidu2")
    def openreport(self):
        self.control.openresult()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
