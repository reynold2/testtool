'''
Created on 2018年7月18日

@author: Administrator
'''
from PIL import ImageGrab,Image

import math
import operator
from functools import reduce
from Tool.CaseData import CaseData
from Tool.GlobalConfig import *
# import win32gui
import ctypes
import sys
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QSystemTrayIcon, QAction, QMenu
from PyQt5.QtCore import Qt, pyqtSignal
from Tool.LoggingConfig import logger



class Photoshop(QMainWindow):
    oksignal = pyqtSignal()

    def __init__(self,sourceroute,address=None,id=None):
        super(Photoshop, self).__init__()
        self.initUI()
        self.id=id
        self.address=address
        self.start = (0, 0)  # 开始坐标点
        self.end = (0, 0)  # 结束坐标点
        self.box=None
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
            # shellTray = win32gui.FindWindow("Shell_TrayWnd", None)
            # win32gui.ShowWindow(shellTray, 0)
            im = ImageGrab.grab()
            im.getbbox()
            im.save(CRimg)
        except:
            logger.error("截图异常")
        finally:
            # win32gui.ShowWindow(shellTray, 1)
            self.sourcedata=CaseData(self.sourcedata)

    def alignment_section(self,Cimg,Rimg):
        excursion=self.image_contrast(Cimg,Rimg)
        result = int(self.image_contrast(Cimg,Rimg))
        logger.info("图片对比偏差：%s"%excursion)
        _max = 5
        _min = 0
        if _max >= result & result >= _min:
            return True
        else:
            return False

    def initUI(self):
        self.setWindowOpacity(0.1)
        self.oksignal.connect(lambda: self.screenshots(self.start, self.end))

    def screenshots(self, start, end,box=None):
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])
        self.box=(x,y,x+width,y+height)
        try:
            if self.address is None:
                fileName = QFileDialog.getSaveFileName(self, '保存图片', '.', ".png;;.jpg")
                if fileName[0]:
                    im = ImageGrab.grab(self.box)
                    im.save(fileName[0] + fileName[1])
                    self.close()
            else:
                im = ImageGrab.grab(self.box)
                im.save(self.address)
                # im.show()
                self.close()
        except:
            logger.error("已取消截图")
        finally:
            self.close()

            CASEDATA[self.id] =self.box
            return self.box
    def Conditions_for_screenshots(self,address=None,box=None):
        if box is None:
            im = ImageGrab.grab()
            im.save(address)
        else:
            im = ImageGrab.grab(box)
            im.save(address)
    def paintEvent(self, event):
        x = self.start[0]
        y = self.start[1]
        w = self.end[0] - x
        h = self.end[1] - y

        pp = QPainter(self)
        pp.drawRect(x, y, w, h)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start = (event.pos().x(), event.pos().y())
            logger.debug('结束坐标：%s', self.start)
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            logger.debug('结束坐标：%s', self.end)
            self.oksignal.emit()
            # 进行重新绘制
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            self.update()


if __name__ == '__main__':
    x=ImageGrab.grab((100,100,300,300))
    print(x.size)
    print(x.getbbox())
    print(x.mode)
    x.save("C:/Users/Administrator/Desktop/1.png")
    z=ImageGrab.grab((100,100,300,300))
    print(z.size)
    print(z.getbbox())
    print(z.mode)
    x.save("C:/Users/Administrator/Desktop/2.png")
    img = Image.open("C:/Users/Administrator/Desktop/1.png")
    print(img.size)
    print(img.getbbox())
    img1 = Image.open("C:/Users/Administrator/Desktop/2.png")
    print(img1.size)
    print(img1.getbbox())
    P = Photoshop("res/RE")
    print(P.image_contrast("C:/Users/Administrator/Desktop/1.png","C:/Users/Administrator/Desktop/2.png"))





