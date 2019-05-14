
from mainwindow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5.QtCore import *
from fileOperation import *
from PyQt5.QtGui import QIcon

class run(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(run, self).__init__(parent)
        self.setupUi(self)
        self.win_signl()
        self.allfilepath=None
        self.setWindowIcon(QIcon("123.ico"))
    def win_signl(self):
        self.Button_FilePath.clicked.connect(self.makelist)
        self.MianButton.clicked.connect(self.mainthread)
        self.FileButton.clicked.connect(self.filerename)
        self.ContextButton.clicked.connect(self.contexrename)
        self.FailButton.clicked.connect(self.failconect)
    def makelist(self):
        self.dialog()
        self.filepath=self.Edit_Path.text()
        if self.allfilepath is None:
            self.allfilepath=wordfilepath(self.CurrentDirPath)
        else:
            self.allfilepath.clear()
            self.allfilepath = wordfilepath(self.CurrentDirPath)

        self.label_5.setText("总计：%s"%str(len(self.allfilepath)))
    def dialog(self):
        self.filepath,suffix=QFileDialog.getOpenFileName()
        if self.filepath is not None:
            fi=QFileInfo(self.filepath)
            self.CurrentDirPath=fi.path()+"/";
            self.Edit_Path.setText(self.CurrentDirPath)
        else:
            pass
    def mainthread(self):
        self.filerename()
        self.contexrename()
        print(faillist)

    def contexrename(self):
        new = self.Edit_Target.text()
        old = self.Edit_Source.text()

        if self.allfilepath is None:
            pass
        else:
            filepool=QThreadPool()
            # filepool.setMaxThreadCount(4)
            for filename in self.allfilepath:
                if os.path.exists(filename):
                    filepool.globalInstance().start(Task(filename,old,new))
                else:
                    print("111111")


    def filerename(self):
        new=self.Edit_Target.text()
        old=self.Edit_Source.text()
        list=[]
        if self.allfilepath is None:
            pass
        else:
            for filename in self.allfilepath:
                a=QFileInfo(filename)
                x=stringrename(a.fileName(), old, new)
                path=os.path.join(a.path(),x)
                QFile.rename(filename,path)
                list.append(path)
        if self.allfilepath is not None:
            self.allfilepath.clear()
            self.allfilepath=list
        else:
            self.allfilepath = list
    def failconect(self):


        text="失败：%i"%(len(faillist))
        text1=self.label_5.text()+text
        self.label_5.setText(text1)
        if faillist is not None:

            self.lineEdit.setText(str(faillist))

            for filename in faillist:
                if os.path.exists(filename):
                    new = self.Edit_Target.text()
                    old = self.Edit_Source.text()
                    x=thread(filename,old,new)
                    x.run()


class thread(QThread):
    def __init__(self,filename,old,new):
        self.old = old
        self.new = new
        self.filename=filename
        super(thread,self).__init__()
    def run(self):
        mianfile(self.filename,self.old,self.new)

class Task(QRunnable):
    def __init__(self,path,old,new):
        self.path=path
        self.old = old
        self.new = new
        super(QRunnable,self).__init__()
    def run(self):
        mianfile(self.path,self.old,self.new)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = run()

    MainWindow.show()
    sys.exit(app.exec_())

