import unittest
from TestTool.WebTestCase.TestCase.OperationPackage import search


class login(unittest.TestCase):
    def setUp(self):
        pass

    def test_baidu1(self):
        '''百度搜索：开'''
        search("开")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()