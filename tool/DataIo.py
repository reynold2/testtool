'''
Created on 2018年7月4日

@author: Administrator
'''
import xlrd
import configparser
import xlwt
import os
from xlutils.copy import copy
import logging
from tool.Gvariable import *


class Excel_io(object):
    # def __init__(self, defaultexcelpath=PATHDATA["case"], **kw):
    def __init__(self,defaultexcelpath=None,**kw):
        self._excelpath = defaultexcelpath
        self.ReadEXcleBasis()
        self.listdata = []


    @property
    def excelpath(self):
        return self._excelpath

    @excelpath.setter
    def excelpath(self, value):
        self._excelpath = value
        return self._excelpath

    def ReadEXcleBasis(self):
        try:

            if os.path.exists(self._excelpath):
                exceldata = xlrd.open_workbook(self._excelpath)
                return exceldata
            else:
                return None
        except:
            return None

    def ReadEXcleData(self):
        self.listdata = []
        if self.ReadEXcleBasis() == None:
            return self.listdata
        else:
            try:
                data = self.ReadEXcleBasis()
                table = data.sheet_by_index(0)
                for h in range(table.nrows):
                    for l in range(table.ncols):
                        self.listdata.append(h)
                        self.listdata.append(l)
                        self.listdata.append(str(table.cell(h, l).value))
                return self.listdata
            except IOError:
                logging.exception("Read File opening exception")
                return self.listdata["1", "1", ""]

    def WriteEXcleData(self, listdata=[], **kw):

        if os.path.exists(self._excelpath):
            pass
        else:
            self._excelpath = "res/report.xls"
            logging.exception(
                "The file does not exist and the default path is used[report.xls]")
        if listdata == self.listdata:
            exceldata = self.ReadEXcleBasis()
            w_xls = copy(exceldata)
            w_xls.save(self._excelpath)
        else:
            try:
                wb = xlwt.Workbook(encoding='utf-8')
                sh = wb.add_sheet("Report")
                for i in range(0, len(listdata), 3):
                    b = listdata[i:i + 3]
                    sh.write(b[0], b[1],
                             b[2])
            except IndexError:
                logging.exception(
                    "File data is lost, incoming data cannot be triples, illegal")
            finally:
                wb.save(self._excelpath)


class Config_io(object):
    def __init__(self, defaultconfigpath="config.ini", **kw):
        self._configpath = defaultconfigpath
        self.confdata = {}

    @property
    def configpath(self):
        return self._configpath

    @configpath.setter
    def configpath(self, value):
        self._configpath = value
# 读取ini返回一个字典

    def ReadConfigData(self):
        try:
            conf = configparser.ConfigParser()
            conf.read(self._configpath, encoding='utf-8-sig')
            hander = conf.sections()
            if "Config" in hander:
                k_v = conf.items('Config')
                self.confdata = dict(k_v)
                return self.confdata
            else:
                k_v = conf.items(hander[0])
                self.confdata = dict(k_v)
                return self.confdata
        except:
            self.confdata = {}
            return self.confdata

    def WriteConfigData(self, outconfdata={}, **kw):
        section = "Config"
        if outconfdata == self.confdata:
            logging.info("Configuration files are not changed to write")
        else:
            self.confdata = outconfdata
            conf = configparser.ConfigParser()
            try:
                conf.add_section(section)
                for key, value in self.confdata.items():
                    conf.set(section, str(key), str(value))
                    try:
                        with open(self._configpath, 'w') as fw:
                            conf.write(fw)
                    except IOError:
                        logging.info(
                            "The file path does not exist and cannot be saved")

            except:
                logging(
                    "File content exception incorrect writing erro")


if __name__ == "__main__":
    c = Config_io()
    e = Excel_io()
    print(c.ReadConfigData())
    print(e.ReadEXcleData())
    c.configpath = "config1.ini"
    e.excelpath = "G:/Python3/layout/tool/RE/report.xls"
    print(e.ReadEXcleData())
    e.excelpath = "G:/Python3/layout/tool/report.xls"
    c.WriteConfigData(outconfdata={"f": 2221})
    e.WriteEXcleData(listdata=[1, 3, 12])
    print(c.ReadConfigData())
