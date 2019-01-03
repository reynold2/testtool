import sqlite3
from openpyxl import load_workbook


class __InitSql__(object):
    daname = "testcase.db"
    testcasepath = "test.xlsx"
    def __init__(self,):

        self.conn = sqlite3.connect(__InitSql__.daname)
        self.cursor = self.conn.cursor()
        self.__InitTestData()
        self.__InitCaseTable()
        self.__InitTestResult()
    def EachXlsx(self):
        wb = load_workbook(__InitSql__.testcasepath)
        ws = wb.worksheets[0]
        for index, row in enumerate(ws.rows):
            if index == 0:
                continue
            yield tuple(map(lambda x: x.value, row))
    def __InitTestData(self):
        CreateTableSql_Test = '''create table "TEST"
          (id_test varchar(20) not null,
            mokuai varchar(20),
            biaoti varchar(100),
            qiwangjieguo varchar(100),
            fujian varchar(20),
            primary key(id_test));'''
        InsertSqlData ="insert into TEST values(?,?,?,?,?)"
        try:
            cursor=self.conn.cursor()
            cursor.execute('''DROP TABLE  IF EXISTS "TEST"''')
            cursor.execute(CreateTableSql_Test)
            self.conn.commit()
        except :
            print("TEST表创建异常")
        finally:
            try:
                cursor.executemany(InsertSqlData,self.EachXlsx())
                self.conn.commit()
            except sqlite3.OperationalError:
                print("TEST数据插入异常")
            finally:
                if cursor:
                    cursor.close()
    def __InitTestResult(self):
        CreateTableSql_Case = '''create table "Result"
            (
            id_test varchar(20), 
            test_name varchar(20),  
            case_name varchar(20),  
            Test_Status varchar(20),
            Result varchar(20) ,
            execution_time varchar(20),
            id_Result integer not null,          
            primary key(id_Result))
            ;  '''
        try:
            cursor = self.conn.cursor()
            cursor.execute('''DROP TABLE  IF EXISTS "Result"''')
            cursor.execute(CreateTableSql_Case)
            self.conn.commit()
        except:
            print("Result数据库表创建异常")
        finally:
            if cursor:
                cursor.close()

    def __InitCaseTable(self):
        CreateTableSql_Case = '''create table "CASE"
            (id_case integer not null,
            method_name varchar(20) ,
            class_name varchar(20),       
            primary key(id_case))

            ;  '''
        try:
            cursor = self.conn.cursor()
            cursor.execute('''DROP TABLE  IF EXISTS "CASE"''')
            cursor.execute(CreateTableSql_Case)
            self.conn.commit()
        except:
            print("case数据库表创建异常")
        finally:
            if cursor:
                cursor.close()
    def __del__(self):
        if self.conn:
            print("初始化完成")
            self.conn.close()


if __name__=="__main__":
    __InitSql__()

