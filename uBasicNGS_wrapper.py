#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-08

import ctypes
from ctypes import *
lib = cdll.LoadLibrary('./libfoo.so')

# Tests with restype
lib.getScore.restype = ctypes.c_float
lib.getScorePosition.restype = ctypes.c_float

class Basic(object):
	def __init__(self, chr="", start=1, end=None, strand=None, score=None):
		if end is None:
			end = start
		if strand is None:
			strand = "FORWARD"
		self.obj = lib.New_basic(chr, start, end, strand)
		if score is not None:
			lib.setScore(self.obj, c_float(score))

	def __del__(self):
		lib.delete_basic(self.obj)

	def getChr(self):
		print c_char_p(lib.getChr(self.obj)).value
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

	def getScoreList(self):
		scoreList = []
		for i in range(0, self.getScoreCount()):
			scoreList.append(self.getScore(i))
		return scoreList

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

	def doesOverlap(self, toCompare):
		return c_bool(lib.doesOverlap(self.obj, toCompare.obj))

	def returnOverlapping(self, toCompare):
		toReturn = Basic()
		toReturn.obj = lib.returnOverlapping(self.obj, toCompare.obj)
		return toReturn

	def returnMerge(self, toCompare):
		toReturn = Basic()
		toReturn.obj = lib.returnMerge(self.obj, toCompare.obj)
		return toReturn
