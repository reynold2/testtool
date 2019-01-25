# -*- coding: UTF-8 -*-
#！usr/bin/python
from TestTool.SqlModel import Model_View
from TestTool.Ui.mianwindow import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from TestTool.threads import RunThread
class MyMainWindow(QMainWindow, Ui_MainWindow):
    run_State_tag=0
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.center = Model_View()
        self.__centralView()
        self.run_quit_action()
    def __centralView(self):
        Q=QWidget()
        H=QHBoxLayout()
        H.addWidget(self.center.modelview())
        self.tab.setLayout(H)
    def run_quit_action(self):
        self.run_Thread=RunThread(0)
        self.run_button=QAction(QIcon("Res/Play_hover.png"), "全部执行", self)
        self.quite_button=QAction(QIcon("Res/终止.png"), "停止", self)
        self.mainToolBar.addActions([self.run_button,self.quite_button])
        self.run_button.triggered.connect(self.run_slot)
        self.quite_button.triggered.connect(self.quite_slot)
    def run_slot(self):
        if MyMainWindow.run_State_tag==0:
        #启动到终止
            self.run_button.setIcon(QIcon("Res/暂停_hover.png"))
            self.run_Thread.start()
            MyMainWindow.run_State_tag = 1
            self.quite_button.setDisabled(False)
            return MyMainWindow.run_State_tag
        elif MyMainWindow.run_State_tag==1:
        #暂停到启动
            self.run_button.setIcon(QIcon("Res/Play_hover.png"))
            self.run_Thread.terminate()
            self.quite_button.setDisabled(True)
            MyMainWindow.run_State_tag = 0
            return MyMainWindow.run_State_tag
    def quite_slot(self):
        self.run_button.setIcon(QIcon("Res/Play_hover.png"))
        self.quite_button.setDisabled(True)
        if MyMainWindow.run_State_tag==1:
            self.run_Thread.terminate()

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
