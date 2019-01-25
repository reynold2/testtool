# -*- coding: UTF-8 -*-
#！usr/bin/python
import os
class Global_Config():
    URL="https://www.baidu.com"
    # URL="http://192.168.43.146:8080/#/login"
    PORT="8080"
    LOGPATH="./log.txt"
    REPORTPATH="Report"
    CASEDIR="WebTestCase"
    BASEPATH=os.path.dirname(__file__)
# 定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
class Element_Config():
    YWJK_config = {
        '登录': {
            '用户名': ['xpath', '/html/body/div/div/form/div[1]/div/div/input'],
            '密码': ['xpath', '/html/body/div/div/form/div[2]/div/div/input'],
            '用户角色': ['xpath', '//input[@value="找找看"]'],
            '登录': ['xpath', '/html/body/div/div/form/div[4]/div/button[1]/span']
        }
    }
    BD_config = {
        '首页搜索': {
            '搜索框': ["id", "kw"],
            '搜索按钮': ["xpath",'''//*[@id="su"]''']
        }
    }



