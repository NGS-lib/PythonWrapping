#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-01

from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self, filename, filetype):
        self.obj = lib.New_parser(filename, filetype)

#    def bar(self):
#        lib.Foo_bar(self.obj)

f = Foo("test.bed", "BED")
#f.bar()
