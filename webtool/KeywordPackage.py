# -*- coding: utf-8 -*-
from webtool.log_config import Logger,LOGER
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webtool.Config import Element_Config
import time

class UIHandle():
    # 构造方法，用来接收selenium的driver对象
    def __init__(self, driver):
        LOGER.logdebug("UIHandle：关键字初始化成功")
        self.driver = driver
    # 输入地址
    def get(self, url):
        LOGER.loginfo(url)
        self.driver.get(url)
    # 关闭浏览器驱动
    def quit(self):
        time.sleep(1)
        self.driver.quit()
    def element(self, page, element):
        # 加入日志
        LOGER.loginfo(page)
        # 加入隐性等待
        # time.sleep(5)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(Element_Config.BD_config[page][element]))
        els = self.driver.find_element(*Element_Config.BD_config[page][element])
        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(Element_Config.YWJK_config[page][element]))
        # els = self.driver.find_element(*Element_Config.YWJK_config[page][element])
        return els
    # send_keys方法
    def Input(self, page, element, msg):
        el = self.element(page, element)
        el.send_keys(msg)
        LOGER.loginfo("输入:%s"%msg)
        LOGER.logdebug("send_keys:page:%s,element:%s,msg:%s"%(page,element,msg))

    # click方法
    def Click(self, page, element):
        el = self.element(page, element)
        el.click()
        LOGER.loginfo("点击成功")
        LOGER.logdebug("Click:page:%s,element:%s"%(page,element))