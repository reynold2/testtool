from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
import time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.base_url = "https://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")
    def test_baidu1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest1")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        pass
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()
