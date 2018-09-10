'''
Created on 2018年7月19日

@author: Administrator
'''
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QGridLayout, QFileDialog, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir,pyqtSignal
from tool.DataManger import MangerData
from time import sleep
from tool.Gvariable import *


class ConfigDialog(QWidget):
    pathchanged = pyqtSignal()
    def __init__(self):
        super(ConfigDialog, self).__init__()
        self.temp = MangerData()
        self.temp.Getconfig()
        self.exceptionfilter()
        self.initUi()

        # print("conf", id(PATHDATA))

    def initUi(self):
        self.setWindowTitle("配置文件")
        self.setGeometry(500, 500, 470, 310)
        self.setWindowIcon(QIcon("res/aboutus.png"))

        label1 = QLabel("用例目录路径:")
        label2 = QLabel("数据文件路径:")
        label3 = QLabel("程序执行路径:")
        label4 = QLabel("测试报告路径:")
        label5 = QLabel("配置文件路径:")

        self.caseLable = QLabel(PATHDATA['case'])
        self.caseLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.dataLable = QLabel(PATHDATA['data'])
        self.dataLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.exeLable = QLabel(PATHDATA['exe'])
        self.exeLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.reportLable = QLabel(PATHDATA['report'])
        self.reportLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.configLable = QLabel(PATHDATA['config'])
        self.configLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        caseButton = QPushButton("浏览")
        caseButton.clicked.connect(self.selectcase)
        dataButton = QPushButton("浏览")
        dataButton.clicked.connect(self.selectdata)
        exeButton = QPushButton("浏览")
        exeButton.clicked.connect(self.selectexe)
        reportButton = QPushButton("浏览")
        reportButton.clicked.connect(self.selectreport)
        configButton = QPushButton("浏览")
        configButton.clicked.connect(self.selectconfig)

        ok = QPushButton("确定")
        ok.clicked.connect(self.Confirmexit)

        mainLayout = QGridLayout()
        mainLayout.addWidget(label1, 0, 0)
        mainLayout.addWidget(self.caseLable, 0, 1)
        mainLayout.addWidget(caseButton, 0, 2)
        mainLayout.addWidget(label2, 1, 0)
        mainLayout.addWidget(self.dataLable, 1, 1)
        mainLayout.addWidget(dataButton, 1, 2)
        mainLayout.addWidget(label3, 2, 0)
        mainLayout.addWidget(self.exeLable, 2, 1)
        mainLayout.addWidget(exeButton, 2, 2)
        mainLayout.addWidget(label4, 3, 0)
        mainLayout.addWidget(self.reportLable, 3, 1)
        mainLayout.addWidget(reportButton, 3, 2)
        mainLayout.addWidget(label5, 4, 0)
        mainLayout.addWidget(self.configLable, 4, 1)
        mainLayout.addWidget(configButton, 4, 2)
        mainLayout.addWidget(ok, 5, 1)

        self.setLayout(mainLayout)
        self.center()

    def exceptionfilter(self):
        if PATHDATA is None:
            PATHDATA['case'] = None
            PATHDATA['data'] = None
            PATHDATA['exe'] = None
            PATHDATA['report'] = None
            PATHDATA['config'] = None
        else:
            pass

    def selectcase(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            if PATHDATA['case'] != filename[0]:
                self.pathchanged.emit()

                PATHDATA['case'] = filename[0]
                self.caseLable.setText(filename[0])
            else:
                pass
            # PATHDATA['case'] = filename[0]
            # self.caseLable.setText(filename[0])
    def selectdata(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            PATHDATA['data'] = filename[0]
            self.dataLable.setText(filename[0])

    def selectexe(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            PATHDATA['exe'] = filename[0]
            self.exeLable.setText(filename[0])

    def selectreport(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            PATHDATA['report'] = filename[0]
            self.reportLable.setText(filename[0])

    def selectconfig(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            PATHDATA['config'] = filename[0]
            self.configLable.setText(filename[0])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Confirmexit(self):
        # print("Confirmexit", PATHDATA)
        self.temp.Setconfig(location=PATHDATA["config"],
                            outconfdata=PATHDATA)

        # print(id(PATHDATA["config"]))
        sleep(0.5)
        self.close()


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    myshow = ConfigDialog()
    myshow.show()
    sys.exit(app.exec_())
