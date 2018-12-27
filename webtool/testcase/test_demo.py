import unittest
from webtool.testcase.OperationPackage import search


class login(unittest.TestCase):
    def setUp(self):
        pass

    def test_baidu1(self):
        search("开")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()