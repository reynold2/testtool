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
class Photoshop(object):
    def __init__(self,sourceroute):
        if PATHDATA.get("data")is not None:
            self.sourcedata=(PATHDATA.get("data"))
        else:
            self.sourcedata=sourceroute
        self.sourcedata=CaseData(sourceroute)
    def image_contrast(self,Cimg,Rimg):
        image1 = Image.open(Cimg)
        image2 = Image.open(Rimg)
        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add,  list(
            map(lambda a, b: (a - b)**2, h1, h2))) / len(h1))
        return result
    def grab(self,CRimg):
        im = ImageGrab.grab()
        im.getbbox()
        im.save(CRimg)
        self.sourcedata=CaseData(self.sourcedata)
    def alignment_section(self,Cimg,Rimg):
        self.image_contrast(Cimg,Rimg)
        result = int(self.image_contrast(Cimg,Rimg))
        _max = 200
        _min = 0
        if _max >= result & result >= _min:
            return True
        else:
            return False
    def casedatacheckout(self):
        pass

if __name__ == '__main__':
    Cimg = "res/RE/a/extension.png"  # 指定图片路径
    Rimg = "res/RE/a/report.png"
    P = Photoshop("res/RE")
    P.grab(Rimg)
    print(P.alignment_section(Cimg,Rimg))







