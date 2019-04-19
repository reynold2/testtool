#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ISmileLi:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):
        print("===in function print_name===")
        print("name:",self.name)

    def print_age(self):
        print("===in function print_age===")
        print("age:",self.age)

    def print_name_age(self):
        print("===in function print_name_age===")
        print("name:%s age:%d" % (self.name,self.age))


def print_message(message):
    print("===in function print_message===")
    print("message:",message)
