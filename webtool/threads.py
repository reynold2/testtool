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
from webtool.ResultManger import Result
from PyQt5.QtWidgets import *
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.t = 0

        window = QWidget()
        vbox = QVBoxLayout(window)
        # vbox = QVBoxLayout(window)

        self.lcdNumber = QLCDNumber()
        button = QPushButton("测试")
        vbox.addWidget(self.lcdNumber)
        vbox.addWidget(button)

        self.timer = QTimer()

        button.clicked.connect(self.Work)
        self.timer.timeout.connect(self.CountTime)

        self.setLayout(vbox)
        self.show()

    def CountTime(self):
        self.t += 1
        self.lcdNumber.display(self.t)

    def Work(self):
        self.timer.start(1000)
        self.thread = RunThread()
        self.thread.start()
        self.thread.trigger.connect(self.TimeStop)

    def TimeStop(self):
        self.timer.stop()
        print("运行结束用时", self.lcdNumber.value())
        self.t = 0


class RunThread(QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    # _signal = pyqtSignal(str)

    trigger = pyqtSignal()



    def __init__(self,casename,parent=None):
        self.casename=casename
        super(RunThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
        # wechat.start_auto(self.callback)
        R=Result()
        R.writresult(self.casename)
        print(self.casename)
        self.trigger.emit()
        # self._signal.emit(msg)

    def callback(self, msg):
        # 信号焕发，我是通过我封装类的回调来发起的
        # self._signal.emit(msg)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    th = Example()
    sys.exit(app.exec_())








