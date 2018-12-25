import unittest
class Casemanger(object):
    def __init__(self,casefilename="testcase"):
        self.lists = casefilename
    def creatsuite(self,lists):
        self.testunit = unittest.TestSuite()
        # discover 方法定义
        discover = unittest.defaultTestLoader.discover(lists, pattern='test_*.py', top_level_dir=None)
        #discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                self.testunit.addTests(test_case)
        return self.testunit
    def GetTestSuite(self,casefilename=None):
        if casefilename:
            __temp = casefilename
        else:
            __temp = self.lists
        return self.creatsuite(__temp)
    def run(self):
        self.GetTestSuite()

if  __name__=="__main__":

    test=Casemanger()
    print(test.GetTestSuite())


