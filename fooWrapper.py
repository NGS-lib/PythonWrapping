#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-01

from ctypes import *
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
	def __init__(self, filename, filetype):
		self.obj = lib.New_parser(filename, filetype)

	def eof(self):
		return c_bool(lib.eof(self.obj))

f = Foo("test.bed", "BED")

if f.eof() == True:
	print "True"
else:
	print "False"
