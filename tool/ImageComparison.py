'''
Created on 2018年7月18日

@author: Administrator
'''
from PIL import ImageGrab,Image
import math
import operator
from functools import reduce
from tool.CaseData import  CaseData

class Photoshop(object):
    def __init__(self,address):
        CaseData()
    def image_contrast(self,imgpath):
        image1 = Image.open(img1)
        image2 = Image.open(img2)
        h1 = image1.histogram()
        h2 = image2.histogram()
        result = math.sqrt(reduce(operator.add,  list(
            map(lambda a, b: (a - b)**2, h1, h2))) / len(h1))
        return result
    def grab(self,imgpath):
        im = ImageGrab.grab()
        im.save(self.img1)
    def alignment_section(self):
        if self.image_contrast()
    def casedatacheckout(self):
        if

if __name__ == '__main__':

    img1 = "res/RE/a/1.png"  # 指定图片路径
    img2 = "res/RE/a/2.png"
    P = Photoshop().image_contrast(img1,img2)
    print(P)







