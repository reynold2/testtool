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

if __name__ == '__main__':
    Cimg = "res/RE/a/extension.png"  # 指定图片路径
    Rimg = "res/RE/a/report.png"
    P = Photoshop("res/RE")
    # P.grab(Rimg)
    print(P.alignment_section(Cimg,Rimg))







