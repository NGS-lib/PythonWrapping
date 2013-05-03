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

class Basic(object):
	def __init__(self, chr, start, end, strand="FORWARD"):
		self.obj = lib.New_basic(chr, start, end, strand)

	def getChr(self):
		return c_char_p(lib.getChr(self.obj)).value

	def setChr(self, chr):
		lib.setChr(self.obj, chr)

# Tests with the parser
f = Foo("test.bed", "BED")
if f.eof() == True:
	print "True"
else:
	print "False"

# Tests with the uBasicNGS
b = Basic("chr1", 100, 200)
print b.getChr()
b.setChr("chr2")
print b.getChr()
