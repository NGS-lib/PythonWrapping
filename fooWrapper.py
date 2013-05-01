#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-01

from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self, toPrint):
        self.obj = lib.Foo_new(toPrint)

    def bar(self):
        lib.Foo_bar(self.obj)

f = Foo("bonjour")
f.bar()
