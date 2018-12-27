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
    def EachXlsx(self):
        wb = load_workbook(__InitSql__.testcasepath)
        ws = wb.worksheets[0]
        for index, row in enumerate(ws.rows):
            if index == 0:
                continue
            yield tuple(map(lambda x: x.value, row))
    def __InitTestData(self):
        CreateTableSql_Test = '''create table "TEST"
          (id_p integer not null,
            lastname varchar(20),
            firstname varchar(20),
            address varchar(100),
            city varchar(100),
            primary key(id_p));'''
        InsertSqlData ="insert into TEST values(?,?,?,?,?)"
        try:
            cursor=self.conn.cursor()
            cursor.execute(CreateTableSql_Test)

            self.conn.commit()
        except:
            print("数据库表已存在")
        finally:
            try:
                cursor.executemany(InsertSqlData,self.EachXlsx())
                self.conn.commit()
            except sqlite3.OperationalError:
                print("TEST数据插入异常")
            finally:
                if cursor:
                    cursor.close()
    def __InitCaseTable(self):
        CreateTableSql_Case = '''create table "CASE"
            (id_o integer not null,
            orderno integer not null,
            id_p integer,
            primary key(id_o),
            foreign key(id_p) references TEST(id_p) on delete cascade on update cascade
            );   '''
        try:
            cursor=self.conn.cursor()
            cursor.execute(CreateTableSql_Case)
            self.conn.commit()
        except:
            print("case数据库表已存在")
        finally:
            if cursor:
                cursor.close()
    def __del__(self):
        if self.conn:
            self.conn.close()


if __name__=="__main__":
    __InitSql__()

