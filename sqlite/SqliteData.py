from PyQt5.QtCore import QTimer
import sqlite3
from time import time
from openpyxl import load_workbook
import re
class SqlDataHandle(object):
    total = 0
    def __init__(self,name="data.db",path="test.xlsx"):
        self.dbname=name
        self.pathexcl=path
        # self.tablesql="create table test(a varchar(0,9999999999),b varchar(0,9999999999),c varchar(0,9999999999),d varchar(0,9999999999),e varchar(0,9999999999))"
        # self.formatsql='insert into test values(?,?,?,?,?)'
        self.tablesql="create table test(a varchar(0,9999999999),b varchar(0,9999999999),c varchar(0,9999999999),d varchar(0,9999999999),e varchar(0,9999999999))"
        self.formatsql='insert into test values(?,?,?,?,?)'
        self.header=None
        self.eachXlsx()
    def eachXlsx(self,pathexcl=None):
        if pathexcl is None:
            __datasql=self.pathexcl
        wb = load_workbook(__datasql)
        ws = wb.worksheets[0]
        # for x in ws.rows:
        #     print(x)
        # print("*"*50**2)
        for index, row in enumerate(ws.rows):
            if index == 0:
                self.header=tuple(map(lambda x:x.value, row))
                # print(self.header)
                continue
            yield tuple(map(lambda x:x.value, row))

    def insertdatasql (self,sqltable=None):
        if sqltable is None:
            __sqltable=self.tablesql
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        try:
            cursor.execute(__sqltable)
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
        self.eachXlsx()
        __sql=[]
        print(len(self.header))
        tablename="table1"
        tablekey="(a varchar(0,9999999999),b varchar(0,9999999999),c varchar(0,9999999999),d varchar(0,9999999999),e varchar(0,9999999999)"

        for  x  in self.header:
            __sql.append(("(%s varchar(0, 9999999999)"%x))

        y=str(("create table %s %s)" % (tablename, (str(__sql).replace("'",""))))).replace("[","").replace("]","")
        print(y)
        new=y[0:y.find("(")]+y[y.find("(")+1:-1]
        # print(new.replace())
        print(new)



    def timer(self):
        start = time()
        self.insertdatasql()
        delta = time() - start
        str=('导入用时：', delta)
        print(str)
    def __call__(self, *args, **kwargs):

        return self
    def run(self):
        y=self.eachXlsx()
        z=self.createtable(y)
        b=self.xlsx2sqlite(z)
        return b




if __name__=="__main__":
    testsql=SqlDataHandle()

    testsql.timer()

    testsql.parsedata()