from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
import time
from webtool.Config import YWJK_config

class login(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.base_url = "http://192.168.43.146:8080/#/login"
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div/div/form/div[1]/div/div/input").clear()
        self.driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div/input").clear()
        # driver.find_element_by_id("kw").send_keys("")
        # driver.find_element_by_id("su").click()
        time.sleep(3)


    def test_zhengchangdenglu(self):
        self.driver.find_element(YWJK_config["登录"]["用户名"]).send_keys("")
        self.driver.find_element(YWJK_config["登录"]["密码"]).send_keys("")
        self.driver.find_element(YWJK_config["登录"]["登录"]).click()
        # self.driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div/div/input").send_keys("")
        # self.driver.find_element_by_xpath("/html/body/div/div/form/div[4]/div/button[1]/span").click()
        time.sleep(10)
        # self.assertEqual(title, u"unittest_百度搜索")
    def test_baidu1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest1")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()