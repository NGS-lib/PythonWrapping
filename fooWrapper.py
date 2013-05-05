#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-01

import ctypes
from ctypes import *
lib = cdll.LoadLibrary('./libfoo.so')

# Tests with restype
lib.getScore.restype = ctypes.c_float
lib.getScorePosition.restype = ctypes.c_float

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

	def getStrand(self):
		return c_char_p(lib.getStrand(self.obj)).value

	def getStart(self):
		return lib.getStart(self.obj)

	def getEnd(self):
		return lib.getEnd(self.obj)

	def getLength(self):
		return lib.getLength(self.obj)

	def getScore(self, position=None):
		if position is None:
			return lib.getScore(self.obj)
		else:
			return lib.getScorePosition(self.obj, position)

	def getScoreCount(self):
		return lib.getScoreCount(self.obj)

	def isReverse(self):
		return c_bool(lib.isReverse(self.obj))

	def setChr(self, chr):
		lib.setChr(self.obj, chr)

	def setStrand(self, strand):
		lib.setStrand(self.obj, strand)

	def setStart(self, start):
		lib.setStart(self.obj, start)

	def setEnd(self, end):
		lib.setEnd(self.obj, end)

	def setStartEnd(self, start, end):
		lib.setStartEnd(self.obj, start, end)

	def setScore(self, score, position=None):
		if position is None:
			lib.setScore(self.obj, c_float(score))
		else:
			lib.setScorePosition(self.obj, c_float(score), position)

	def extendSite(self, extendLeft, extendRight=None):
		if extendRight is None:
			lib.extendSite(self.obj, extendLeft)
		else:
			lib.extendSiteLeftRight(self.obj, extendLeft, extendRight)

	def trimSite(self, trimLeft, trimRight=None):
		if trimRight is None:
			lib.trimSite(self.obj, trimLeft)
		else:
			lib.trimSiteLeftRight(self.obj, trimLeft, trimRight)

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

print b.getStrand()
b.setStrand("-")
print b.getStrand()

print "**** Start/End/Length tests with set/get/extend/trim"
print "Base Values"
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Length: " + str(b.getLength())
print "setStart(50), setEnd(250)"
b.setStart(50)
b.setEnd(250)
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Length: " + str(b.getLength())
print"setStartEnd(75,125)"
b.setStartEnd(75,125)
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Length: " + str(b.getLength())
print "extendSite(10)"
b.extendSite(10)
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Length: " + str(b.getLength())
print "trimSite(30)"
b.trimSite(30)
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Length: " + str(b.getLength())
print "extendSite(10,20)"
b.extendSite(10,20)
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Length: " + str(b.getLength())
print "trimSite(5,10)"
b.trimSite(5,10)
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Length: " + str(b.getLength())

print "**** Score tests"
#print "Score: " + str(b.getScore())
print "ScoreCount: " + str(b.getScoreCount())
print "setScore(100.2)"
b.setScore(100.3)
print "Score: " + str(b.getScore())
print "ScoreCount: " + str(b.getScoreCount())
b.setScore(233.24, 1)
print "Score(0): " + str(b.getScore(0))
print "Score(1): " + str(b.getScore(1))
print "ScoreCount: " + str(b.getScoreCount())
