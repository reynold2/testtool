import unittest
from webtool.Config import Global_Config
from webtool.threads import func_arg
class Casemanger(object):
    def __init__(self,casefilename=Global_Config.CASEDIR):
        self.lists = casefilename
        self.GetTestSuite()
    def creatsuite(self,lists):
        self.testunit = unittest.TestSuite()
        # discover 方法定义
        discover = unittest.defaultTestLoader.discover(lists, pattern='test_*.py', top_level_dir=None)
        #discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                print(test_case)
                self.testunit.addTests(test_case)
        return self.testunit
    #自定义获取那个文件夹中符合pattern='test_*.py'的测试用例，返回一个测试套件
    def GetTestSuite(self,casefilename=None):
        if casefilename:
            __temp = casefilename
        else:
            __temp = self.lists
        return self.creatsuite(__temp)
    def run(self):
        self.GetTestSuite()
    # @func_arg(arg=True,num=2)
    # def test(self,x):
    #     print(self.testunit)
    #     return x

if  __name__=="__main__":

    test=Casemanger()
    test.test(1)


