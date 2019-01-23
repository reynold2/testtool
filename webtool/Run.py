# -*- coding: UTF-8 -*-
#！usr/bin/python
from webtool.SqlModel import Model_View
from webtool.ui.mianwindow import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.changewindows()
    def changewindows(self):
        QWidget(self.centralwidget)
        self.widget=Model_View().modelview()

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
