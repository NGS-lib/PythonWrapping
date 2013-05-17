#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-08

import ctypes
from ctypes import *
#lib = cdll.LoadLibrary("/home/local/USHERBROOKE/nora2001/Work/libs/release/libpyThonWrap.so")
lib = cdll.LoadLibrary('./libfoo.so')

# Tests with restype
lib.getScore.restype = ctypes.c_float

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

	def get_chr(self):
		return c_char_p(lib.getChrBasic(self.obj)).value

	def get_strand(self):
		return c_char_p(lib.getStrand(self.obj)).value

	def get_start(self):
		return lib.getStart(self.obj)

	def get_end(self):
		return lib.getEnd(self.obj)

	def get_length(self):
		return lib.getLength(self.obj)

	def get_score(self, position=None):
		if position is None:
			return lib.getScore(self.obj)
		else:
			return lib.getScorePosition(self.obj, position)

	def get_score_count(self):
		return lib.getScoreCount(self.obj)

	def get_score_list(self):
		scoreList = []
		for i in range(0, self.get_score_count()):
			scoreList.append(self.get_score(i))
		return scoreList

	def is_reverse(self):
		return c_bool(lib.isReverse(self.obj))

	def set_chr(self, chr):
		lib.setChr(self.obj, chr)

	def set_strand(self, strand):
		lib.setStrand(self.obj, strand)

	def set_start(self, start):
		lib.setStart(self.obj, start)

	def set_end(self, end):
		lib.setEnd(self.obj, end)

	def set_start_end(self, start, end):
		lib.setStartEnd(self.obj, start, end)

	def set_score(self, score, position=None):
		if position is None:
			lib.setScore(self.obj, c_float(score))
		else:
			lib.setScorePosition(self.obj, c_float(score), position)

	def extend_site(self, extendLeft, extendRight=None):
		if extendRight is None:
			lib.extendSite(self.obj, extendLeft)
		else:
			lib.extendSiteLeftRight(self.obj, extendLeft, extendRight)

	def trim_site(self, trimLeft, trimRight=None):
		if trimRight is None:
			lib.trimSite(self.obj, trimLeft)
		else:
			lib.trimSiteLeftRight(self.obj, trimLeft, trimRight)

	def does_overlap(self, toCompare):
		return c_bool(lib.doesOverlap(self.obj, toCompare.obj))

	def return_overlapping(self, toCompare):
		toReturn = Basic()
		toReturn.obj = lib.returnOverlapping(self.obj, toCompare.obj)
		return toReturn

	def return_merge(self, toCompare):
		toReturn = Basic()
		toReturn.obj = lib.returnMerge(self.obj, toCompare.obj)
		return toReturn

if __name__=="__main__":
	# Tests with the uBasicNGS
	print "**** Tests constructor basic"
	b = Basic()
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor chr"
	b = Basic("chr1")
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor start"
	b = Basic("chr1", 1000)
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor end"
	b = Basic("chr1", 1000, 1200)
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor strand"
	b = Basic("chr1", 1000, 1200, "-")
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor score"
	b = Basic("chr1", 1000, 1200, "-", 2.4)
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "Score: " + str(b.get_score())

	print "**** Misc tests"
	b = Basic("chr1", 100, 200)
	print b.get_chr()
	b.set_chr("chr2")
	print b.get_chr()

	print b.get_strand()
	b.set_strand("-")
	print b.get_strand()
	print "IsReverse: " + str(b.is_reverse())

	print "**** Start/End/Length tests with set/get/extend/trim"
	print "Base Values"
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Length: " + str(b.get_length())
	print "set_start(50), set_end(250)"
	b.set_start(50)
	b.set_end(250)
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Length: " + str(b.get_length())
	print"set_start_end(75,125)"
	b.set_start_end(75,125)
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Length: " + str(b.get_length())
	print "extend_site(10)"
	b.extend_site(10)
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Length: " + str(b.get_length())
	print "trim_site(30)"
	b.trim_site(30)
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Length: " + str(b.get_length())
	print "extend_site(10,20)"
	b.extend_site(10,20)
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Length: " + str(b.get_length())
	print "trim_site(5,10)"
	b.trim_site(5,10)
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Length: " + str(b.get_length())

	print "**** Score tests"
	#print "Score: " + str(b.get_score())
	print "ScoreCount: " + str(b.get_score_count())
	print "set_score(100.2)"
	b.set_score(100.3)
	print "Score: " + str(b.get_score())
	print "ScoreCount: " + str(b.get_score_count())
	b.set_score(233.24, 1)
	print "Score(0): " + str(b.get_score(0))
	print "Score(1): " + str(b.get_score(1))
	print "ScoreCount: " + str(b.get_score_count())
	print "ScoreList: " + str(b.get_score_list())

	print "**** Tests for does_overlap"
	b2 = Basic("chr2", 100, 200)
	b3 = Basic("chr2", 201, 300)
	b4 = Basic("chr1", 100, 200)
	print "does overlap: " + str(b.does_overlap(b2))
	print "does not overlap: " + str(b.does_overlap(b3))
	print "does overlap not same chr: " + str(b.does_overlap(b4))

	print "**** Tests for returnOverlapping"
	c = b.return_overlapping(b2)
	print "Overlap: chr: " + c.get_chr()
	print "Overlap: start: " + str(c.get_start())
	print "Overlap: end: " + str(c.get_end())

	print "**** Tests for return_merge"
	c = b.return_merge(b2)
	print "Merge: chr: " + c.get_chr()
	print "Merge: start: " + str(c.get_start())
	print "Merge: end: " + str(c.get_end())
