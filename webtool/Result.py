from webtool.HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.chrome.webdriver import WebDriver
from webtool.CaseManger import Casemanger
import unittest

class Result(Casemanger):
    def __init__(self):
        super().__init__()
    def writresult(self):
        alltestnames=self.GetTestSuite()
        fp = open('./result.html', 'wb')
        runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
        runner.run(alltestnames)
        fp.close()
        return
    @staticmethod
    def openresult():
        driver = WebDriver()
        driver.get("file:///D:/git_workspace/testtool/webtool/result.html")
    def run_report(self):
        self.writresult()
    def run(self):
        unittest.TextTestRunner().run(self.GetTestSuite())
    def run_open_repoet(self):
        self.writresult()
        self.openresult()


if __name__=="__main__":
    test=Result()
    test.run()





