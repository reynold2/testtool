import sqlite3
from sqlite.execl import x
class sql(object):
    def __init__(self,data=None):
        self.data=data
        self.datalist=x()
        # self.datalist.read_excel()[1]
        # self.exchange()
    def insert(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        print(self.datalist.read_excel())
        cursor.execute("create table test(z varchar(20),x varchar(20),c varchar(30),v varchar(30))")

        sql = 'insert into test(z,x,c,v) values(?,?,?,?)'
        cursor.executemany(sql, self.datalist.read_excel())

        conn.commit()
        conn.close()

    def exchange(self):
        z=len(self.datalist.read_excel())
        for x in z:

            return tuple(x)

        return z
    def encode(self,dat):
        dat.encode("gbk")
        dat.uncode("UTF-8")
        return dat


x=sql()
x.insert()