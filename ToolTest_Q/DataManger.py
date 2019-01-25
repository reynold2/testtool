'''
Created on 2018年7月4日

@author: Administrator
'''
from ToolTest_Q.DataIo import Excel_io, Config_io
from ToolTest_Q.GlobalConfig import *


class MangerData(object):
    def __init__(self):
        self.E = Excel_io()
        self.E.excelpath
        self.p = Config_io()
        self.p.configpath
    def GetExcel(self, location=None, **kwargs):
        self.E.excelpath = location
        return self.E.ReadEXcleData()
    def SetExcel(self, location=None, datalist=[]):
        self.E.excelpath = location
        return self.E.WriteEXcleData(listdata=datalist)
    def Getconfig(self, location=PATHDATA["config"]):
        self.p.configpath = location
        PATHDATA["TestCase"] = self.p.ReadConfigData()["TestCase"]
        PATHDATA["config"] = self.p.ReadConfigData()["config"]
        PATHDATA["report"] = self.p.ReadConfigData()["report"]
        PATHDATA["exe"] = self.p.ReadConfigData()["exe"]
        PATHDATA["data"] = self.p.ReadConfigData()["data"]
        return self.p.ReadConfigData()

    def Setconfig(self, location=PATHDATA["config"], outconfdata=None):
        self.p.configpath = location

        return self.p.WriteConfigData(outconfdata)

    def GetModelData(self):
        return

    def ShowView(self):
        return


if __name__ == "__main__":
    #     print(MangerData().GetExcel(location="TestData.xls"))
    zx = MangerData()
#     zx.Setconfig(outconfdata={"asd": "12"})
#     zx.SetExcel(location="", datalist=[1, 1, 8])
#     print(MangerData().Getconfig())
