'''
Created on 2018年7月6日

@author: Administrator
'''

import os
import shutil


class CaseData(object):
    def __init__(self, path="G:\\Python3\\layout\\tool\\RE"):
        self.path = path
        self.dirset = set()
        self.exsionset = set()
        self.resourceset = set()
        self.filedit = {}

    def dir(self):
        try:
            for parent, dirnames, filenames in os.walk(self.path,  followlinks=False):
                for x in dirnames:
                    self.dirset.add(x)
            return self.dirset
        except OSError as reason:
            print('出错啦！' + str(reason))

    def exsionresource(self):
        for parent, dirnames, filenames in os.walk(self.path,  followlinks=False):
            for filename in filenames:
                if filename == "extension.xml":
                    file_path = os.path.join(parent, filename)
                    self.exsionset.add(file_path)
                elif filename == "PrintScreen.png":
                    file_path = os.path.join(parent, filename)
                    self.resourceset.add(file_path)
                else:
                    pass
        return self.exsionset, self.resourceset

#     def key_key_value(self):
#         for parent, dirnames, filenames in os.walk(self.path,  followlinks=False):
#             for dir in dirnames:
#                 print(dir)
#                 print(len(dirnames))
#                 self.filedit[dirnames[x]] = os.path.join(
#                     parent, filename)
#             for x in range(len(dirnames)):
#                 print(x)
#                 for filename in filenames:
#                     # if os.path.join(parent, filename) != None:
#                     self.filedit[dirnames[x]] = os.path.join(
#                         parent, filename)
#                     print(self.filedit)
# #                     else:
# #                         continue
#         print(self.filedit)


print(CaseData().key_key_value())
