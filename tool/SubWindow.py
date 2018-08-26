'''
Created on 2018年7月6日

@author: Administrator
'''

import os

from TableWidget import CentralView


class CaseData(CentralView):
    def __init__(self, path="G:\\Python3\\layout\\tool\\RE"):

        self.path = path
        self.dirset = set()
        self.dirlist = []
        self.exsionlist = []
        self.resourcelist = []
        self.exsiondit = {}
        self.resourcedit = {}
        self.dir()
        self.exsionresource()
        self._dirset()

    def dir(self):
        try:
            for parent, dirnames, filenames in os.walk(self.path,  followlinks=False):
                for x in dirnames:
                    self.dirlist.append(x)
            return self.dirlist
        except OSError as reason:
            print('出错啦！' + str(reason))

    def exsionresource(self):
        for parent, dirnames, filenames in os.walk(self.path,  followlinks=False):
            for filename in filenames:
                if filename == "extension.xml":
                    file_path = os.path.join(parent, filename)
                    self.exsionlist.append(file_path)
                elif filename == "PrintScreen.png":
                    file_path = os.path.join(parent, filename)
                    self.resourcelist.append(file_path)
                else:
                    pass
        return self.exsionlist, self.resourcelist

    def key_value(self):
        for x in range(len(self.dirlist)):
            self.exsiondit[self.dirlist[x]] = self.exsionlist[x]
        for x in range(len(self.dirlist)):
            self.resourcedit[self.dirlist[x]] = self.resourcelist[x]
        return self.exsiondit, self.resourcedit

    def _dirset(self):
        self.dirset = set(self.dirlist)
        return self.dirset


print(CaseData().key_value())
