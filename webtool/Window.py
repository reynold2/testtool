'''
Created on 2018年7月4日

@author: Administrator
'''
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class UI(QMainWindow):
    def __init__(self, parent=None):
        super(UI,self).__init__(parent)
        self.__window__()
    def __window__(self):
        self.__menuBar()
        self.__toolbar()
        self.__dockview()
        self.__centerview()
        self.setGeometry(100, 100, 1120, 750)
        self.setWindowTitle("Test")
        self.show()
    def __menuBar(self):
        pass
    def __toolbar(self):
        tb=self.addToolBar("toolbar")

    def __dockview(self):
        pass
    def __centerview(self):
        pass








if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
