from webtool.HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.chrome.webdriver import WebDriver
from webtool.Config import Global_Config
from webtool.CaseManger import Casemanger
import unittest
import time



class Result(Casemanger):
    def __init__(self):
        super().__init__()
    def writresult(self):
        alltestnames=self.GetTestSuite()

        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))

        filename = Global_Config.REPORTPATH+"/" + now + '_result.html'  # 定义个报告存放路径，支持相对路径。
        self.filename=filename
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
        runner.run(alltestnames)

        fp.close()
        return self.filename
    def openresult(self,report=None):
        import webbrowser
        if report:
            print("需要拼接地址")
        else:
            webbrowser.open(
                    "file:///D:/git_workspace/testtool/webtool/Report/result.html", new=0, autoraise=True)
        # driver.get("file:///D:/git_workspace/testtool/webtool/result.html")

    def run_report(self):
        self.writresult()

    def run(self):
        unittest.TextTestRunner().run(self.GetTestSuite())
    def run_open_repoet(self):
        self.writresult()
        self.openresult()


if __name__=="__main__":
    test=Result()
    test.run_open_repoet()





