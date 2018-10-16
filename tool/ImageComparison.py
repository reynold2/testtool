'''
Created on 2018年7月18日

@author: Administrator
'''
from PIL import ImageGrab,Image
import math
import operator
from functools import reduce
from tool.CaseData import CaseData
from tool.Gvariable import *
import win32gui
import ctypes
import sys
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QSystemTrayIcon, QAction, QMenu
from PyQt5.QtCore import Qt, pyqtSignal
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_int),
                ('top', ctypes.c_int),
                ('right', ctypes.c_int),
                ('bottom', ctypes.c_int)]


class Photoshop(object):
    def __init__(self,sourceroute):
        if PATHDATA.get("data")is not None:
            self.sourcedata=(PATHDATA.get("data"))
        else:
            self.sourcedata=sourceroute
        self.sourcedata=CaseData(sourceroute)
    def image_contrast(self,Cimg,Rimg):
        try:
            image1 = Image.open(Cimg)
            image2 = Image.open(Rimg)
            h1 = image1.histogram()
            h2 = image2.histogram()
            result = math.sqrt(reduce(operator.add,  list(
                map(lambda a, b: (a - b)**2, h1, h2))) / len(h1))
            return result
        except:
            return 9999
    def grab(self,CRimg):
        try:
            shellTray = win32gui.FindWindow("Shell_TrayWnd", None)
            win32gui.ShowWindow(shellTray, 0)
            im = ImageGrab.grab()
            im.getbbox()
            im.save(CRimg)
            # rect = RECT()
            # HWND = win32gui.GetForegroundWindow()
            # ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))  # 获取当前窗口坐标
            # coordinate = (rect.left + 2, rect.top + 2, rect.right - 2, rect.bottom - 2)  # 转换为预截图窗口坐标
            # im = ImageGrab.grab(coordinate)
            # im.getbbox()
            # im.save(CRimg)
        except:
            print("截图异常")
        finally:
            win32gui.ShowWindow(shellTray, 1)
            self.sourcedata=CaseData(self.sourcedata)
    def alignment_section(self,Cimg,Rimg):
        excursion=self.image_contrast(Cimg,Rimg)
        result = int(self.image_contrast(Cimg,Rimg))
        print("图片对比偏差：%s"%excursion)
        _max = 5
        _min = 0
        if _max >= result & result >= _min:
            return True
        else:
            return False
    def casedatacheckout(self):
        pass
    def checkout(self):
        pass
    def position(self,point,CRimg):
        im = ImageGrab.grab(point)
        im.getbbox()
        im.save(CRimg)



class MyWin(QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.initUi()

    def initUi(self):
        # 窗口大小设置为600*500
        self.setWindowTitle("截图")
        self.resize(200, 100)
        self.btn = QPushButton('截图', self)
        self.btn.setGeometry(20, 20, 60, 60)
        self.btn.clicked.connect(self.click_btn)

        self.addSystemTray()  # 设置系统托盘

    def addSystemTray(self):
        minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        maximizeAction = QAction("Ma&ximize", self, triggered=self.showMaximized)
        restoreAction = QAction("&Restore", self, triggered=self.showNormal)
        quitAction = QAction("&Quit", self,
                             triggered=self.close)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(minimizeAction)
        self.trayIconMenu.addAction(maximizeAction)
        self.trayIconMenu.addAction(restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("icon.png"))
        self.setWindowIcon(QIcon("icon.png"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()

    def click_btn(self):
        self.showMinimized()
        self.screenshot = ScreenShotsWin()
        self.screenshot.showFullScreen()


class ScreenShotsWin(QMainWindow):
    # 定义一个信号
    oksignal = pyqtSignal()

    def __init__(self):
        super(ScreenShotsWin, self).__init__()
        self.initUI()
        self.start = (0, 0)  # 开始坐标点
        self.end = (0, 0)  # 结束坐标点

    def initUI(self):
        # self.showFullScreen()
        self.setWindowOpacity(0.4)
        self.btn_ok = QPushButton('保存', self)


        self.oksignal.connect(lambda: self.screenshots(self.start, self.end))

    def screenshots(self, start, end):
        '''
        截图功能
        :param start:截图开始点
        :param end:截图结束点
        :return:
        '''
        logger.debug('开始截图,%s, %s', start, end)

        x = min(start[0], end[0])
        y = min(start[1], end[1])
        g=(end[0] - start[0])
        h=(end[1] - start[1])

        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])

        des = QApplication.desktop()
        screen = QApplication.primaryScreen()
        if screen:
            self.setWindowOpacity(0.0)
            pix = screen.grabWindow(des.winId(), x, y, width, height)

        fileName = QFileDialog.getSaveFileName(self, '保存图片', '.', ".png;;.jpg")
        if fileName[0]:
            pix.save(fileName[0] + fileName[1])

        self.close()

    def paintEvent(self, event):
        '''
        给出截图的辅助线
        :param event:
        :return:
        '''
        logger.debug('开始画图')
        x = self.start[0]
        y = self.start[1]
        w = self.end[0] - x
        h = self.end[1] - y

        pp = QPainter(self)
        pp.drawRect(x, y, w, h)

        logger.debug('x:%s,y:%s,w:%s,h:%s'%(x, y, w, h))
    def mousePressEvent(self, event):

        # 点击左键开始选取截图区域
        if event.button() == Qt.LeftButton:
            self.start = (event.pos().x(), event.pos().y())
            logger.debug('开始坐标：%s', self.start)

    def mouseReleaseEvent(self, event):

        # 鼠标左键释放开始截图操作
        if event.button() == Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            logger.debug('结束坐标：%s', self.end)

            self.oksignal.emit()
            logger.debug('信号提交')
            # 进行重新绘制
            self.update()

    def mouseMoveEvent(self, event):

        # 鼠标左键按下的同时移动鼠标绘制截图辅助线
        if event.buttons() and Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            logger.debug('正在移动：%s', self.end)
            # 进行重新绘制
            self.update()

# if __name__ == '__main__':
#     Cimg = "res/RE/a/extension.png"  # 指定图片路径
#     Rimg = "res/RE/a/report.png"
#     P = Photoshop("res/RE")
#     # P.grab(Rimg)
#     print(P.alignment_section(Cimg,Rimg))






# 定义结构体，存储当前窗口坐标

if __name__ == '__main__':
    # Cimg = "res/RE/a/extension.png"  # 指定图片路径
    # Rimg = "res/RE/a/report.png"
    # P = Photoshop("res/RE")
    # # P.grab(Rimg)
    # print(P.alignment_section(Cimg,Rimg))
    # s=(324,103,117,143)
    # P = Photoshop("res/RE")
    # P.position(s)
    # ImageGrab.grab((474,256,267,257)).show()

    # rect = RECT()
    # HWND = win32gui.GetForegroundWindow()
    # ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))  # 获取当前窗口坐标
    # coordinate = (rect.left + 2, rect.top + 2, rect.right - 2, rect.bottom - 2)  # 转换为预截图窗口坐标
    # print(coordinate)
    # pic = ImageGrab.grab(coordinate)  # 截图
    # pic.show()

    app = QApplication(sys.argv)
    dbb = MyWin()
    dbb.show()
    sys.exit(app.exec_())





