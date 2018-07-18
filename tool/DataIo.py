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


class excel_io(object):
    def __init__(self, defaultexcelpath="G:/Python3/layout/test/config/case/TestData1.xls", **kw):
        self.excelpath = defaultexcelpath
        self.ReadEXcleBasis()

    @property
    def excelpathproperty(self):
        return self.excelpath

    @excelpathproperty.setter
    def excelpathproperty(self, value):
        self.excelpath = value
        return self.excelpath

    def ReadEXcleBasis(self):
        if os.path.exists(self.excelpath):
            exceldata = xlrd.open_workbook(self.excelpath)
            return exceldata
        else:
            logging.exception("The file does not exist under the current path")

    def ReadEXcleData(self):
        # 返回字典
        #ditdata = {}
        listdata = []
        try:
            data = self.ReadEXcleBasis()
            table = data.sheet_by_index(0)
            for h in range(table.nrows):
                for l in range(table.ncols):
                            # 返回字典
                    #ditdata[h, l] = table.cell(h, l).value
                    listdata.append(h)
                    listdata.append(l)
                    listdata.append(table.cell(h, l).value)
            return listdata
        except IOError:
            logging.exception("Read File opening exception")

    def WriteEXcleData(self, ischangecontent=False, loc="G:/Python3/layout/tool/RE/report.xls", listdata=[], **kw):
        if os.path.exists(loc):
            pass
        else:
            loc = "report.xls"
            logging.exception("File path exception")
        if ischangecontent == False:
            exceldata = self.ReadEXcleBasis()
            w_xls = copy(exceldata)
            w_xls.save(loc)
        else:
            try:
                wb = xlwt.Workbook(encoding='utf-8')
                sh = wb.add_sheet("Report")
                for i in range(0, len(listdata), 3):
                    b = listdata[i:i + 3]
                    sh.write(b[0], b[1],
                             b[2])
                wb.save(loc)
            except IOError:
                logging.exception("File write exception")


class config_io(object):
    def __init__(self, defaultconfigpath="config.ini", **kw):
        self.configpath = defaultconfigpath

    @property
    def configpathproperty(self):
        return self.configpath

    @configpathproperty.setter
    def configpathproperty(self, value):
        self.configpath = value
# 读取ini返回一个字典

    def ReadConfigData(self):
        try:
            conf = configparser.ConfigParser()
            conf.read(self.configpath, encoding='utf-8-sig')
            hander = conf.sections()
            if "config" in hander:
                k_v = conf.items('config')
                confdata = dict(k_v)
                return confdata
            else:
                k_v = conf.items(hander[0])
                confdata = dict(k_v)
                return confdata
        except:
            return None

    def WriteConfigData(self, defaultloc="config.ini", section="config", confdata=None, **kw):
        conf = configparser.ConfigParser()
        try:
            conf.add_section(section)
            for key, value in confdata.items():
                conf.set(section, key, value)
            with open(defaultloc, 'w') as fw:
                conf.write(fw)
        except:
            return None
