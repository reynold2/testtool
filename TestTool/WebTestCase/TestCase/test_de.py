import unittest
from TestTool.WebTestCase.TestCase.OperationPackage import search


class login1(unittest.TestCase):
    def setUp(self):
        pass

    def test_baidu2(self):
        search("开")
    def test_baidu3(self):
        search("i")
        # self.assertEqual("i", u"unittest_百度搜索")
    def tearDown(self):
        pass
        # if sys.exc_info()[0]:
        #     test_method_name = self._testMethodName
        #     self.driver.save_screenshot("%s.png" % test_method_name)
        # super(login1, self).tearDown()


if __name__ == "__main__":
    unittest.main()