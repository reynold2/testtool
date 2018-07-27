'''
Created on 2018年7月19日

@author: Administrator
'''
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QGridLayout, QFileDialog, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir
from DataManger import MangerData


class ConfigDialog(QWidget):

    def __init__(self):
        super(ConfigDialog, self).__init__()
        self.model = ConfigModel()
        self.model.datadit
        self.model.Register(self)
        self.initUi()
        self.exceptionfilter()
        self.list = {}

    def update(self, model):
        #         self.list = model.datalist
        #         return self.list
        pass

    def initUi(self):
        self.setWindowTitle("配置文件")
        self.setGeometry(500, 500, 470, 310)
        self.setWindowIcon(QIcon("res/aboutus.png"))

        label1 = QLabel("用例目录路径:")
        label2 = QLabel("数据文件路径:")
        label3 = QLabel("程序执行路径:")
        label4 = QLabel("测试报告路径:")
        label5 = QLabel("配置文件路径:")

        self.caseLable = QLabel(self.model.datadit['case'])
        self.caseLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.dataLable = QLabel(self.model.datadit['data'])
        self.dataLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.exeLable = QLabel(self.model.datadit['exe'])
        self.exeLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.reportLable = QLabel(self.model.datadit['report'])
        self.reportLable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.configLable = QLabel(self.model.datadit['config'])
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
        if self.model.datadit == None:
            self.model.datadit['case'] = None
            self.model.datadit['data'] = None
            self.model.datadit['exe'] = None
            self.model.datadit['report'] = None
            self.model.datadit['config'] = None
            return self.model.valueChanged(self.model.datadit)
        else:
            pass

    def selectcase(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            self.model.datadit['case'] = filename[0]
            self.caseLable.setText(self.model.datadit['case'])
        return self.model.valueChanged(self.model.datadit)

    def selectdata(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            self.model.datadit['data'] = filename[0]
            self.dataLable.setText(self.model.datadit['data'])
        return self.model.valueChanged(self.model.datadit)

    def selectexe(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            self.model.datadit['exe'] = filename[0]
            self.exeLable.setText(self.model.datadit['exe'])
        return self.model.valueChanged(self.model.datadit)

    def selectreport(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            self.model.datadit['report'] = filename[0]
            self.reportLable.setText(self.model.datadit['report'])
        return self.model.valueChanged(self.model.datadit)

    def selectconfig(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.AnyFile)
        file.setFilter(QDir.Files)
        if file.exec_():
            filename = file.selectedFiles()
            self.model.datadit['config'] = filename[0]
            self.configLable.setText(self.model.datadit['config'])
        return self.model.valueChanged(self.model.datadit)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Confirmexit(self):
        print(self.model.datadit.items())

        self.close()


class DataoBserved(object):

    def __init__(self):
        self._observers = []

    def Register(self, observer):
        self._observers.append(observer)
        observer.update(self)

    def Unregiter(self, observer):
        self._observers.remove(observer)

    def NotilyObservers(self):
        for observer in self._observers:
            observer.update(self)


class ConfigModel(DataoBserved):
    def __init__(self):
        super(ConfigModel, self).__init__()
        x = MangerData()
        self.datadit = x.Getconfig(location="config.ini")

    def valueChanged(self, datadit):
        if self.datadit != datadit:
            self.datadit = datadit
            self.NotilyObservers()


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    myshow = ConfigDialog()
    myshow.show()
    sys.exit(app.exec_())
