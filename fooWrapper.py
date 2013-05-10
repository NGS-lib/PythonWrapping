#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-01

from ctypes import *
from uBasicNGS_wrapper import *
from uBasicNGSChrom_wrapper import *
lib = cdll.LoadLibrary('./libfoo.so')

# Tests with restype
#lib.New_basicScore.argtypes = [ c_char_p, c_int, c_int, c_char_p, c_float ]
lib.getScore.restype = ctypes.c_float
lib.getScorePosition.restype = ctypes.c_float

class Foo(object):
	def __init__(self, filename, filetype):
		self.obj = lib.New_parser(filename, filetype)

	def eof(self):
		return c_bool(lib.eof(self.obj))

# Tests with the parser
f = Foo("test.bed", "BED")
if f.eof() == True:
	print "True"
else:
	print "False"

# Tests with the uBasicNGS

print "**** Tests constructor basic"
b = Basic()
print "Chr: " + b.getChr()
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Strand: " + str(b.getStrand())
print "**** Tests constructor chr"
b = Basic("chr1")
print "Chr: " + b.getChr()
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Strand: " + str(b.getStrand())
print "**** Tests constructor start"
b = Basic("chr1", 1000)
print "Chr: " + b.getChr()
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Strand: " + str(b.getStrand())
print "**** Tests constructor end"
b = Basic("chr1", 1000, 1200)
print "Chr: " + b.getChr()
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Strand: " + str(b.getStrand())
print "**** Tests constructor strand"
b = Basic("chr1", 1000, 1200, "-")
print "Chr: " + b.getChr()
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Strand: " + str(b.getStrand())
print "**** Tests constructor score"
b = Basic("chr1", 1000, 1200, "-", 2.4)
print "Chr: " + b.getChr()
print "Start: " + str(b.getStart())
print "End: " + str(b.getEnd())
print "Strand: " + str(b.getStrand())
print "Score: " + str(b.getScore())

print "**** Misc tests"
b = Basic("chr1", 100, 200)
print b.getChr()
b.setChr("chr2")
print b.getChr()

print b.getStrand()
b.setStrand("-")
print b.getStrand()
print "IsReverse: " + str(b.isReverse())

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
print "ScoreList: " + str(b.getScoreList())

print "**** Tests for doesOverlap"
b2 = Basic("chr2", 100, 200)
b3 = Basic("chr2", 201, 300)
b4 = Basic("chr1", 100, 200)
print "does overlap: " + str(b.doesOverlap(b2))
print "does not overlap: " + str(b.doesOverlap(b3))
print "does overlap not same chr: " + str(b.doesOverlap(b4))

print "**** Tests for returnOverlapping"
c = b.returnOverlapping(b2)
print "Overlap: chr: " + c.getChr()
print "Overlap: start: " + str(c.getStart())
print "Overlap: end: " + str(c.getEnd())

print "**** Tests for returnMerge"
c = b.returnMerge(b2)
print "Merge: chr: " + c.getChr()
print "Merge: start: " + str(c.getStart())
print "Merge: end: " + str(c.getEnd())

print "--------------------------"
print "TESTS: uBasicNGSChrom"
print "--------------------------"
print "**** Tests for constructor"
chrom = Chrom()
chromName = Chrom("chr5")
chromNameSize = Chrom("chr3", 123456)
chromSize = Chrom(chromosomeSize=123456)
