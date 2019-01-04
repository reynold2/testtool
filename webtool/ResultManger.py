from webtool.HTMLTestRunner import HTMLTestRunner
from webtool.Config import Global_Config
from webtool.log_config import LOGER
from webtool.CaseManger import Casemanger
import unittest
import time
import os
import sys

class Result(Casemanger):
    def __init__(self):
        super(Result,self).__init__()
    def writresult(self,casename):
        if self.testcasedit.get(casename):
            alltestnames = self.testcasedit.get(casename)
        else:
            alltestnames=self.GetTestSuite()
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
        filename = Global_Config.REPORTPATH+"/" + now + '_result.html'  # 定义个报告存放路径，支持相对路径。
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
        runner.run(alltestnames)
        fp.close()
        return filename
    def openresult(self,report=None):
        LOGER.loginfo(sys.argv)
        import webbrowser
        if report:
            LOGER.logdebug("需要拼接地址")
            pass
        else:
            LocalWebPath="file:///%s/%s/%s"%(Global_Config.BASEPATH,Global_Config.REPORTPATH,self.getnewreport())
            webbrowser.open(
                LocalWebPath, new=0, autoraise=True)
        # driver.get("file:///D:/git_workspace/testtool/webtool/result.html")
    def getnewreport(self):
        lists=os.listdir("report")
        lists.sort(key= lambda f:os.path.getatime("report"+"\\"+f))
        newfilename=lists[-1]
        LOGER.logdebug("最新报告：%s"%newfilename)
        return newfilename
    def run_report(self):
        self.writresult()
    def run(self):
        unittest.TextTestRunner().run(self.GetTestSuite())
    def run_open_repoet(self):
        self.writresult()
        self.openresult()


if __name__=="__main__":
    test=Result()

    # test.writresult("yu")





