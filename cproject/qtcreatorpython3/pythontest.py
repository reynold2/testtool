#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hello(s):
    print("hello world")
    print(s)


def arg(a, b):
    print('a=', a)
    print('b=', b)
    return a + b


class Test:
    name=""
    def __init__(self,name):
        slef.init=name
        print("init111"+name)

    def say_hello(self, can1,can2):
        print("hello", slef.init,can1,can2)
#        return name
    def hello(self):
        print("hhhh")
