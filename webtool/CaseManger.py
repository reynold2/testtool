import unittest
from webtool.Config import Global_Config
from webtool.log_config import LOGER
class Casemanger(object):
    def __init__(self,casefilename=Global_Config.CASEDIR):
        self.casefilename = casefilename
        self.__testcase()
    def __testcase(self):
        self.testcasedit = {}
        # discover 方法定义
        discover = unittest.defaultTestLoader.discover(self.casefilename, pattern='test_*.py', top_level_dir=None)
        #discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                for x in test_case:
                    key=x.__str__()
                    self.testcasedit[key]=x
        return self.testcasedit
    #自定义获取那个文件夹中符合pattern='test_*.py'的测试用例，返回一个测试套件
    def GetTestSuite(self,casename=None):
        testunit = unittest.TestSuite()
        if casename is None:
            testunit.addTests(self.testcasedit.values())
        else:
            if self.testcasedit.get(casename):
                testunit.addTest(self.testcasedit.get(casename))
            else:
                LOGER.logdebug("名称为:%s当前case不存在"%casename)
        return testunit
    def GetTestSuiteList(self,list=None):
        self.GetTestSuite()

    # def run(self,*kw):



if  __name__=="__main__":

    test=Casemanger()
    print(test.testcasedit)
    # test.test(1)


