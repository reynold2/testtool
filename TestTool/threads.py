# -*- coding: utf-8 -*-
# from  webtool.ResultManger import Result
# def func_arg(arg =False,num=3):
#     if arg:
#         def func(funNume):
#             print(funNume)
#             def func_in(*args,**kargs):
#                 print(*args,**kargs)
#                 return funNume(*args,**kargs)
#             return func_in
#         return func
#     else:
#         def func(funNume):
#             def func_in(*args,**kargs):
#                 return funNume(*args,**kargs)
#             return func_in
#         return func
from PyQt5.QtCore import *
from TestTool.ResultManger import Result
from PyQt5.QtWidgets import *
import sys


# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.t = 0
#
#         window = QWidget()
#         vbox = QVBoxLayout(window)
#         # vbox = QVBoxLayout(window)
#
#         self.lcdNumber = QLCDNumber()
#         button = QPushButton("测试")
#         vbox.addWidget(self.lcdNumber)
#         vbox.addWidget(button)
#
#         self.timer = QTimer()
#
#         button.clicked.connect(self.Work)
#         self.timer.timeout.connect(self.CountTime)
#
#         self.setLayout(vbox)
#         self.show()
#
#     def CountTime(self):
#         self.t += 1
#         self.lcdNumber.display(self.t)
#
#     def Work(self):
#         self.timer.start(1000)
#         self.thread = RunThread()
#         self.thread.start()
#         self.thread.trigger.connect(self.TimeStop)
#
#     def TimeStop(self):
#         self.timer.stop()
#         print("运行结束用时", self.lcdNumber.value())
#         self.t = 0


class RunThread(QThread):
    thread_signal = pyqtSignal()

    def __init__(self,casename,parent=None):
        self.casename=casename
        super(RunThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
        R=Result()
        R.writresult(self.casename)
        self.thread_signal.emit()
if __name__ == "__main__":
    th = RunThread()
    th.run()









