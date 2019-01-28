'''
Created on 2018年7月6日

@author: Administrator
'''
import os
import time
import subprocess
from PyQt5.QtCore import QThread, pyqtSignal
from ToolTest_Q.GlobalConfig import *
from ToolTest_Q.CaseData import CaseData
from ToolTest_Q.LoggingConfig import logger


def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)  # 取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
            logger.info('正在移除文件: ' + path_file)
        else:
            del_file(path_file)


def delete_gap_dir(path):

    if os.path.isdir(path):
        for d in os.listdir(path):
            delete_gap_dir(os.path.join(path, d))
    if not os.listdir(path):
        os.rmdir(path)
        logger.info('正在移除空目录: ' + path)


class Runexe(QThread):
    cout={}
    sinOut = pyqtSignal()
    def __init__(self, args):
        self.args= args
        self.data=CaseData(PATHDATA.get('data'))
        super(Runexe, self).__init__()
    def run(self):
        z, f = os.path.split(PATHDATA.get('exe'))
        configfilepath = z + "/config"
        if type(self.args)is list:
            for x in self.args:
                logger.debug("当前正在执行的测试用例：%s",x)
                if os.path.exists(configfilepath) is True:
                    os.system('TASKKILL /F /IM %s'%f)
                    del_file(configfilepath)
                    delete_gap_dir(configfilepath)
                    self.data.copyexsiondit(x)
                    if PATHDATA.get('exe') is None:
                        logger.warn("执行文件路径不能为空，程序无法启动")
                    else:
                        subprocess.call(PATHDATA["exe"])
                        self.sinOut.emit()
                        logger.info("测试程序已停止运行")

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
                    logger.warn("执行文件路径不能为空，程序无法启动")
                else:
                    subprocess.call(PATHDATA["exe"])
                    logger.info("测试程序已停止运行")
    @classmethod
    def handling(cls):
        return cls.cout


if __name__ == "__main__":
    ex = Runexe()
    ex.run()
