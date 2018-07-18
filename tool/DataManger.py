'''
Created on 2018年7月4日

@author: Administrator
'''
from DataIo import *
import operator


class MangerData(object):
    def __init__(self):
        self.E = excel_io()
        self.p = config_io()

    def GetExcel(self):
        return self.E.ReadEXcleData()

    def SetExcel(self, ischangecontent="", loc="", listdata=""):

        return self.E.WriteEXcleData(ischangecontent, loc, listdata)

    def Getconfig(self):
        return

    def Setconfig(self, path):

        return

    def DataComparison(self, table="", excel=""):
        table = self.GetModelData
        excel = self.GetExcel
        return operator.eq(table, excel)

    def GetModelData(self):
        return

    def UpdateModeData(self):
        return

    def ShowView(self):
        return


# print(MangerData().GetExcel())
