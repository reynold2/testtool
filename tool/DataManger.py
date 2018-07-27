'''
Created on 2018年7月4日

@author: Administrator
'''
from DataIo import excel_io, config_io


# class Subject(object):
#
#     def __init__(self):
#         self._observers = []
#
#     def attach(self, observer):
#         if observer not in self._observers:
#             self._observers.append(observer)
#
#     def detach(self, observer):
#         try:
#             self._observers.remove(observer)
#         except ValueError:
#             pass
#
#     def notify(self, modifier=None):
#         for observer in self._observers:
#             if modifier != observer:
#                 observer.update(self)


# Example usage
# class Data(Subject):
#
#     def __init__(self, name=''):
#         Subject.__init__(self)
#         self.name = name
#         self._data = 0
#
#     @property
#     def data(self):
#         return self._data
#
#     @data.setter
#     def data(self, value):
#         self._data = value
#         self.notify()


# class HexViewer:
#
#     def update(self, subject):
#         print(u'HexViewer: Subject %s has data 0x%x' %
#               (subject.name, subject.data))
#
#
# class DecimalViewer:
#
#     def update(self, subject):
#         print(u'DecimalViewer: Subject %s has data %d' %
#               (subject.name, subject.data))


class MangerData(object):
    def __init__(self):
        self.E = excel_io()
        self.E.excelpath
        self.p = config_io()
        self.p.configpath
#         self.s = []

    def GetExcel(self, location="TestData.xls", **kwargs):
        self.E.excelpath = location
        return self.E.ReadEXcleData()

    def SetExcel(self, location="report.xls", datalist=[]):
        self.E.excelpath = location
        return self.E.WriteEXcleData(listdata=datalist)

    def Getconfig(self, location="config.ini"):
        self.p.configpath = location
        return self.p.ReadConfigData()

    def Setconfig(self, location="config.ini", datadit={}):
        self.p.configpath = location
        return self.p.WriteConfigData(confdata=datadit)

    def GetModelData(self):
        return

#     def update(self, mode):
#         self.s = self.s + mode
#         return self.s

    def ShowView(self):
        return


if __name__ == "__main__":
    print(MangerData().GetExcel(location="TestData.xls"))
#     MangerData().Setconfig(datadit={"asd": "ds"})
#     MangerData().SetExcel(location="", datalist=[1, 2, 3])
    print(MangerData().Getconfig(location="config.ini"))
