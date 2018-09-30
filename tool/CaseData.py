'''
Created on 2018年7月6日

@author: Administrator
'''

import os
from tool.Gvariable import *
import shutil


class CaseData(object):
    _obj = None
    _init_flag=True
    def __new__(cls, *args, **kw):
        if not cls._obj:
            cls._obj = object.__new__(cls)
        return cls._obj
    def __init__ (self, path):
        self.path = path
        if CaseData._init_flag:
            self.dirset = set()
            self.dirlist = []
            self.exsionlist = []
            self.resourcelist = []
            self.resourcelist1=[]
            self.resourcedit1={}
            self.exsiondit = {}
            self.resourcedit = {}
            self.dir()
            self.exsionresource()
            self._dirset()
            CaseData._init_flag = False

    def dir(self):
        try:
            for parent, dirnames, filenames in os.walk(self.path,  followlinks=False):
                for x in dirnames:
                    self.dirlist.append(x)
            return self.dirlist
        except OSError as reason:
            print('出错啦！' + str(reason))

    def exsionresource(self):
        exsionlist = []
        resourcelist = []
        resourcelist1=[]
        for parent, dirnames, filenames in os.walk(self.path,  followlinks=False):

            for filename in filenames:
                if filename == "extension.xml":
                    file_path = os.path.join(parent, filename)
                    exsionlist.append(file_path)
                elif filename == "extension.png":
                    file_path = os.path.join(parent, filename)
                    resourcelist.append(file_path)
                elif filename == "report.png":
                    file_path = os.path.join(parent, filename)
                    resourcelist1.append(file_path)

        self.exsionlist =list({}.fromkeys(exsionlist).keys())
        self.resourcelist = list({}.fromkeys(resourcelist).keys())
        self.resourcelist1 = list({}.fromkeys(resourcelist1).keys())

        return self.exsionlist,self.resourcelist,self.resourcelist1

    def key_value(self):
        if len(self.exsionlist) == len(self.dirlist):
            for x in range(len(self.dirlist)):
                self.exsiondit[self.dirlist[x]] = self.exsionlist[x]
        else:
            print("测试数据不完整，请检查")
        if len(self.dirlist) == len(self.resourcelist):
            for x in range(len(self.dirlist)):
                self.resourcedit[self.dirlist[x]] = self.resourcelist[x]
        else:
            print("测试数据资源不完整，请检查")
        if len(self.dirlist) == len(self.resourcelist1):
            for x in range(len(self.dirlist)):
                self.resourcedit1[self.dirlist[x]] = self.resourcelist1[x]
        else:
            print("测试结论数据被破坏不完整，请检查")
        return self.exsiondit, self.resourcedit, self.resourcedit1

    def _dirset(self):
        self.dirset = set(self.dirlist)
        return self.dirset
    def copyexsiondit (self,id="a"):
        z, f = os.path.split(PATHDATA.get('exe'))
        targetpath = z + "/plugins/tech.microcore.mainwin.desktop/extension.xml"
        extensoinpath=self.key_value()[0].get(id)
        if extensoinpath is not None:
            print(extensoinpath)
            print(targetpath)
            shutil.copyfile(extensoinpath,targetpath)
        else:
            pass

    def copyresourcedit(self):
        pass

if __name__=="__main__":

    print(CaseData("res/RE").key_value())
