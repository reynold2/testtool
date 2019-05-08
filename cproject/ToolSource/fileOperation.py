#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32com.client
import os
import time
import win32com
# 处理Word文档的类

#执行次数
num=0

class RemoteWord:
    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('Word.Application')  # 此处使用的是Dispatch，原文中使用的DispatchEx会报错
        self.xlApp.Visible = 0  # 后台运行，不显示
        self.xlApp.DisplayAlerts = 0 # 不警告
        if filename:
            self.filename = filename
            if os.path.exists(self.filename):
                self.doc = self.xlApp.Documents.Open(filename)
            else:
                self.doc = self.xlApp.Documents.Add() # 创建新的文档
                self.doc.SaveAs(filename)
        else:
            self.doc = self.xlApp.Documents.Add()
            self.filename = ''
    def add_doc_end(self, string):
        '''在文档末尾添加内容'''
        rangee = self.doc.Range()
        rangee.InsertAfter('\n' + string)
    def add_doc_start(self, string):
        """在文档开头添加内容"""
        rangee = self.doc.Range(0, 0)
        rangee.InsertBefore(string + '\n')
    def insert_doc(self, insertPos, string):
        '''在文档insertPos位置添加内容'''

        rangee = self.doc.Range(0, insertPos)
        if (insertPos == 0):
            rangee.InsertAfter(string)
        else:
            rangee.InsertAfter('\n' + string)
    def replace_doc(self, string, new_string):
        '''替换文字'''
        self.xlApp.Selection.Find.ClearFormatting()
        self.xlApp.Selection.Find.Replacement.ClearFormatting()
        self.xlApp.Selection.Find.Execute(string, False, False, False, False, False, True, 1, True, new_string, 2)
        # (string--搜索文本,
        # True--区分大小写,
        # True--完全匹配的单词，并非单词中的部分（全字匹配）,
        # True--使用通配符,
        # True--同音,
        # True--查找单词的各种形式,
        # True--向文档尾部搜索,
        # 1,
        # True--带格式的文本,
        # new_string--替换文本,
        # 2--替换个数（全部替换）
    def replace_docs(self, string, new_string):
        '''采用通配符匹配替换'''
        self.xlApp.Selection.Find.ClearFormatting()
        self.xlApp.Selection.Find.Replacement.ClearFormatting()
        self.xlApp.Selection.Find.Execute(string, False, False, True, False, False, False, 1, False, new_string, 2)
    def header(self,string, new_string):
        Sections=self.xlApp.ActiveDocument.Sections
        for Section in Sections:
            for Header in Section.Headers:
                Header.Range.Find.ClearFormatting()
                Header.Range.Find.Replacement.ClearFormatting()
                Header.Range.Find.Execute(string, False, False, False, False, False, True, 1,
                                                          False, new_string, 2)
    def save(self):
        '''保存文档'''
        self.doc.Save()

    def save_as(self, filename):
        '''文档另存为'''
        self.doc.SaveAs(filename)

    def close(self):
        '''保存文件、关闭文件'''
        self.save()
        self.xlApp.Documents.Close()
        self.xlApp.Quit()

    def word_replace(self,string, new_string):
        '''替换内容和页眉'''
        self.header(string, new_string)
        self.replace_doc(string, new_string)
        self.close()


class RemoteExcel():
    """对excel表格的操作

    """
    def __init__(self, filename=None):
        """初始化函数

        Args:
            filename: 要进行操作的文件名，如果存在此文件则打开，不存在则新建
                        此文件名一般包含路径

        """
        self.xlApp=win32com.client.Dispatch('Excel.Application')
        self.xlApp.Visible=0
        self.xlApp.DisplayAlerts=0    #后台运行，不显示，不警告
        if filename:
            self.filename=filename
            if os.path.exists(self.filename):
                self.xlBook=self.xlApp.Workbooks.Open(filename)
            else:
                self.xlBook = self.xlApp.Workbooks.Add()    #创建新的Excel文件
                self.xlBook.SaveAs(self.filename)
        else:
            self.xlBook=self.xlApp.Workbooks.Add()
            self.filename=''

    def get_cell(self, row, col, sheet=None):
        """读取单元格的内容

        Args:
            row: 行
            col: 列
            sheet: 表格名（不是文件名）

        """
        if sheet:
            sht = self.xlBook.Worksheets(sheet)
        else:
            sht = self.xlApp.ActiveSheet
        return sht.Cells(row, col).Value

    def set_cell(self, sheet, row, col, value):
        """向表格单元格写入

        Args:
            sheet: 表格名（不是文件名）
            row: 行
            col: 列
            value: 定入内容
        """
        try:
            sht = self.xlBook.Worksheets(sheet)
        except:
            self.new_sheet(sheet)
            sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value

    def save(self, newfilename=None):
        """保存表格"""
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(self.filename)
        else:
            self.xlBook.Save()

    def close(self):
        """保存表格、关闭表格，结束操作"""
        self.save()
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp

    def new_sheet(self, newSheetName):
        """新建一个新表格"""
        sheet = self.xlBook.Worksheets.Add()
        sheet.Name = newSheetName
        sheet.Activate()

    def active_sheet(self):
        return self.xlApp.ActiveSheet

    def re_Excel(self,dizhi,old,new):
        self.xlBook = self.xlApp.Workbooks.Open(dizhi)
        for Worksheet in self.xlBook.Worksheets:
            Rows=Worksheet.UsedRange.Rows.Count
            Columns=Worksheet.UsedRange.Columns.Count
            for Row in range(Rows):
                for Column in range(Columns):
                    text=Worksheet.Cells(Row+1, Column+1).Value
                    if type(text) is float:
                        Worksheet.Cells(Row+1, Column+1).Value=str(int(text)).replace(str(old),str(new))
                    elif type(text) is str:
                        if old in text:
                            Worksheet.Cells(Row+1, Column+1).Value=text.replace(old,new)
                    else:
                        if str(old) in str(text):
                            Worksheet.Cells(Row+1, Column+1).Value=str(text).replace(old,new)
        self.save()
        self.close()



def mianfile(path, old, new):
    if os.path.isfile(path):
        suffix=os.path.splitext(path)[-1]
        if suffix == ".xlsx":
            try:
                hell(path, old, new)
                return 1
            except:
                pass
        elif suffix == ".docx":
            try:
                word(path, old, new)
                # time.sleep(5)
                return 1
            except:
                pass
        else:
            return 2

def hell(dizhi,old,new):
    import win32com.client

    xlApp = win32com.client.Dispatch('Excel.Application')
    xlApp.Visible = 0
    xlApp.DisplayAlerts = 0
    if os.path.exists(dizhi):
        xlBook =xlApp.Workbooks.Open(dizhi)
    else:
        xlBook = xlApp.Workbooks.Add()  # 创建新的Excel文件
        xlBook.SaveAs(dizhi)

    for Worksheet in xlBook.Worksheets:
        Rows = Worksheet.UsedRange.Rows.Count
        Columns = Worksheet.UsedRange.Columns.Count
        for Row in range(Rows):
            for Column in range(Columns):
                text = Worksheet.Cells(Row + 1, Column + 1).Value
                if type(text) is float:
                    Worksheet.Cells(Row + 1, Column + 1).Value = str(int(text)).replace(str(old), str(new))
                elif type(text) is str:
                    if old in text:
                        Worksheet.Cells(Row + 1, Column + 1).Value = text.replace(old, new)
                else:
                    if str(old) in str(text):
                        Worksheet.Cells(Row + 1, Column + 1).Value = str(text).replace(old, new)

    xlBook.Save()
    xlBook.Close(SaveChanges=0)
    return 3
def word(dizhi,old,new):
    xlApp = win32com.client.Dispatch('Word.Application')  # 此处使用的是Dispatch，原文中使用的DispatchEx会报错
    xlApp.Visible = 0  # 后台运行，不显示
    xlApp.DisplayAlerts = 0  # 不警告
    if dizhi:
        if os.path.exists(dizhi):
            doc = xlApp.Documents.Open(dizhi)
        else:
            doc = xlApp.Documents.Add()  # 创建新的文档
            doc.SaveAs(dizhi)
    Sections1=xlApp.ActiveDocument.Sections
    for Section1 in Sections1:
        for Header1 in Section1.Headers:
            Header1.Range.Find.ClearFormatting()
            Header1.Range.Find.Replacement.ClearFormatting()
            Header1.Range.Find.Execute(old, False, False, False, False, False, True, 1,
                                                          False, new, 2)

    xlApp.Selection.Find.ClearFormatting()
    xlApp.Selection.Find.Replacement.ClearFormatting()
    xlApp.Selection.Find.Execute(old, False, False, False, False, False, True, 1, True, new, 2)

    doc.Save()
    xlApp.Documents.Close()
    xlApp.Quit()






if __name__=='__main__':
    #example1
    # mianfile("E:\\test\\新建 Microsoft Excel 工作表.xlsx","啊","旧")


    # excel = RemoteExcel('D:\\test\\新建 Microsoft Excel 工作表.xlsx')
    # excel.re_Excel("啊啊","123")
    # word = RemoteWord()
    # word.word_replace("E:\\test\\新建 Microsoft Word 文档.docx","123","wo")
    # hell("E:\\test\\wz.xlsx","o","sss")
    mianfile("E:\\test\\wz - 副本.docx","文","付")


