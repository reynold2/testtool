'''
Created on 2018年7月4日

@author: Administrator
'''
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout
import sys
from webtool.SqlModel import Model_View

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
        layout=QHBoxLayout()
        layout.addWidget(self.view())
        self.setLayout(layout)
        self.setWindowTitle("Test")
        self.setCentralWidget(self.view())
        self.show()
    def __menuBar(self):
        pass
    def view(self):
        x = Model_View()
        z=x.modelview()
        return z
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
