'''
Created on 2018年7月4日

@author: Administrator
'''
import sys
from Tool.MainWindow import Window
from PyQt5.QtWidgets import QApplication



class Run(Window):
    def __init__(self):
        super().__init__()
    # def __del__(self):
    #     print("1")
    #     object.__del__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Run()
    sys.exit(app.exec_())

