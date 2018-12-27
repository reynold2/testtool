from webtool.KeywordPackage import UIHandle
from webtool.Config import Global_Config
from selenium.webdriver.chrome.webdriver import WebDriver

# 打开博客园首页，进行找找看搜索功能
def search(msg):
    # 打开浏览器
    driver =WebDriver()
    # 传入driver对象
    uihandle = UIHandle(driver)
    #输入url地址
    uihandle.get(Global_Config.URL)
    # 调用二次封装后的方法，此处可见操作了哪个页面，哪个元素，msg是要插入的值，插入值得操作在另外一个用例文件中传入
    uihandle.Input("首页搜索","搜索框", msg)
    uihandle.Click('首页搜索', '搜索按钮')
    uihandle.quit()