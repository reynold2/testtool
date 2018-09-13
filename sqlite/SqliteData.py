from PyQt5.QtCore import QTimer
import sqlite3
from time import time
from openpyxl import load_workbook
import os
import re
class SqlDataHandle(object):
    total = 0
    def __init__(self,name="data.db",path="test.xlsx"):
        self.dbname=name
        self.pathexcl=path
        self.tablesql="create table test(a varchar(0,9999999999),b varchar(0,9999999999),c varchar(0,9999999999),d varchar(0,9999999999),e varchar(0,9999999999))"
        self.formatsql='insert into test values(?,?,?,?,?)'
        self.header =None
    def eachXlsx(self,pathexcl=None):
        __header=[]
        if pathexcl is None:
            __datasql = self.pathexcl
        else:
            if str(pathexcl).endswith(".xlsx") is not False:
                __datasql=self.pathexcl
        wb = load_workbook(__datasql)
        ws = wb.worksheets[0]
        for index, row in enumerate(ws.rows):
            if index == 0:
                self.header=tuple(map(lambda x: x.value, row))
                continue
            yield tuple(map(lambda x: x.value, row))

    def insertdatasql (self,sqltable=None):
        if sqltable is None:
            sqltable = self.tablesql
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        try:
            cursor.execute(sqltable)
        except sqlite3.OperationalError:
            print("table test already exists")
        finally:
            cursor.executemany(self.formatsql, self.eachXlsx())
            conn.commit()
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def parsedata(self,*agre):
        self.eachXlsx().__next__()
        __Tsql=[]
        __Dsql = []
        z, f = os.path.split(self.pathexcl)
        tablename =f[0:-5]
        for x in self.header:
            __Tsql.append(("%s varchar(0, 80000)" % x))
            __Dsql.append("?")
        self.tablesql= str(("create table %s (%s)" % (tablename, (str(__Tsql).replace("'", ""))))).replace("[", "").replace("]", "")
        self.formatsql=str("insert into %s values(%s)"%(tablename, str(__Dsql).replace("'", ""))).replace("[", "").replace("]", "")
        return self.tablesql




    def timer(self,fun):
        start = time()
        fun()
        delta = time() - start
        print('导入用时：', delta)
    def __call__(self, *args, **kwargs):
        print("将对象变成可回调")
        return self
    def default_run(self):
        self.insertdatasql(self.parsedata())




if __name__=="__main__":
    testsql=SqlDataHandle()
    testsql.default_run()