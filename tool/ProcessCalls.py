'''
Created on 2018年7月6日

@author: Administrator
'''
import os
import time
import subprocess
from PyQt5.QtCore import QThread, pyqtSignal
from tool.Gvariable import *
from tool.CaseData import CaseData

def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)  # 取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
            print('正在移除文件: ' + path_file)
        else:
            del_file(path_file)


def delete_gap_dir(path):

    if os.path.isdir(path):
        for d in os.listdir(path):
            delete_gap_dir(os.path.join(path, d))
    if not os.listdir(path):
        os.rmdir(path)
        print('正在移除空目录: ' + path)


class runexe(QThread):
    cout={}
    sinOut = pyqtSignal()
    def __init__(self, args):
        self.args= args
        self.data=CaseData(PATHDATA.get('data'))
        super(runexe, self).__init__()
    def run(self):
        z, f = os.path.split(PATHDATA.get('exe'))
        configfilepath = z + "/config"
        if type(self.args)is list:
            for x in self.args:
                print(x)
                if os.path.exists(configfilepath) is True:
                    os.system('TASKKILL /F /IM %s'%f)
                    del_file(configfilepath)
                    delete_gap_dir(configfilepath)
                    self.data.copyexsiondit(x)
                    if PATHDATA.get('exe') is None:
                        print("执行文件路径不能为空，程序无法启动")
                    else:
                        subprocess.call(PATHDATA["exe"])
                        self.sinOut.emit()

                        print("测试程序已停止运行")
                else:
                    pass
                time.sleep(1)
        else:
            if os.path.exists(configfilepath) is True:
                os.system('TASKKILL /F /IM %s'%f)
                del_file(configfilepath)
                delete_gap_dir(configfilepath)
                self.data.copyexsiondit(self.args)
                if PATHDATA.get('exe') is None:
                    print("执行文件路径不能为空，程序无法启动")
                else:
                    subprocess.call(PATHDATA["exe"])
                    print("测试程序已停止运行")
    @classmethod
    def handling(cls):
        return cls.cout


if __name__ == "__main__":
    ex = runexe()
    ex.run()
