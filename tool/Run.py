'''
Created on 2018年7月4日

@author: Administrator
'''
import sys
from tool.MainWindow import window
from PyQt5.QtWidgets import QApplication


class run(window):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = run()
    sys.exit(app.exec_())
