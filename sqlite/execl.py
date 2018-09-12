import xlrd

class x(object):
    def __init__(self,path="TestData1.xls"):
        self.path=path
    def read_excel(self):
        list=[]
        workbook = xlrd.open_workbook(self.path)
        sheet_name = workbook.sheet_names()[0]
        sheet = workbook.sheet_by_name(sheet_name)
        for x in range(sheet.nrows):
            # list.append(tuple(map(lambda x:x.encode("utf-8"),sheet.row_values(x))))
            list.append(tuple(sheet.row_values(x)))
        return list






