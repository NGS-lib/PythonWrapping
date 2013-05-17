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
print "No param:"
chrom = Chrom()
print "chr: " + chrom.getChr()
print "chrSize: " + str(chrom.getChromSize())
print "Chrom Name"
chromName = Chrom("chr5")
print "chr: " + chromName.getChr()
print "chrSize: " + str(chromName.getChromSize())
print "Chrom Name Size:"
chromNameSize = Chrom("chr3", 123456)
print "chr: " + chromNameSize.getChr()
print "chrSize: " + str(chromNameSize.getChromSize())
print "Chrom Size:"
chromSize = Chrom(chromosomeSize=123456)
print "chr: " + chromSize.getChr()
print "chrSize: " + str(chromSize.getChromSize())

print "**** Tests for getCopy"
chromCopy = chromNameSize.getCopy()
print "chr: " + chromCopy.getChr()
print "chrSize: " + str(chromCopy.getChromSize())

print "**** Tests for addData functions"
chromAddData = Chrom("chr3")
basicAddData = Basic("chr3", 100, 200)
chromAddData.addData(basicAddData)
print "chr: " + chromAddData.getChr()
print "chrSize: " + str(chromAddData.getChromSize())

print "**** Tests for inferChrSize "
chromInfer = Chrom("chr3")
chromInfer.addData(Basic("chr3", 1000, 3000))
print "chrSize (before): " + str(chromInfer.getChromSize())
chromInfer.inferChrSize()
print "chrSize (after): " + str(chromInfer.getChromSize())
chromInfer = Chrom()
print "chrSize (empty):" + str(chromInfer.getChromSize())

print "**** Tests for the divideItemsIntoNBins function"
chromDivide = Chrom("chr4")
chromDivide.addData(Basic("chr4", 1000, 3000))
print "count (before): " + str(chromDivide.count())
chromDivide.divideItemsIntoNBins(10, "IGNORE")
print "count (after): " + str(chromDivide.count())

print "**** Tests for the divideItemsIntoBinofSize function"
chromDivide = Chrom("chr4")
chromDivide.addData(Basic("chr4", 1000, 2000))
print "count (before): " + str(chromDivide.count())
chromDivide.divideItemsIntoBinofSize(20, "IGNORE")
print "count (after): " + str(chromDivide.count())

print "**** Tests for the function getSite"
chromGetSite = Chrom("chr1")
chromGetSite.addData(Basic("chr1", 300, 500))
aSite = chromGetSite.getSite(0)
print "getSite: chr: " + aSite.getChr()
print "getSite: start: " + str(aSite.getStart())
print "getSite: end: " + str(aSite.getEnd())

print "**** Tests for the statistic functions"
chromStats = Chrom("chrX")
chromStats.addData(Basic("chrX", 300, 500))
chromStats.addData(Basic("chrX", 300, 600))
chromStats.addData(Basic("chrX", 400, 500))
print "avg: " + str(chromStats.avgSiteSize())
print "min: " + str(chromStats.minSiteSize())
print "max: " + str(chromStats.maxSiteSize())
print "sum: " + str(chromStats.sumSiteSize())
print "count: " + str(chromStats.count())

#print "**** Tests for adding random sites"
#chromAddRandom = Chrom("chrY")
#chromAddRandom.addRandomSites(100, 10)
#print "Count: " + str(chromAddRandom.count())

print "**** Tests for getOverlapping/getOverlappingCount"
chromOverlap1 = Chrom("chr1")
chromOverlap1.addData(Basic("chr1", 100, 200))
chromOverlap1.addData(Basic("chr1", 400, 800))
chromOverlap1.addData(Basic("chr1", 1000, 1200))
print "Different chrom:"
chromOverlap2 = Chrom("chr2")
chromOverlap2.addData(Basic("chr2", 100, 200))
chromOverlap2.addData(Basic("chr2", 400, 800))
chromOverlap2.addData(Basic("chr2", 1000, 1200))
chromOverlapResult = chromOverlap1.getOverlapping(chromOverlap2)
print "Result Count: " + str(chromOverlapResult.count())
print "getOverlapCount: " + str(chromOverlap1.getOverlappingCount(chromOverlap2))
print "No overlap:"
chromOverlap3 = Chrom("chr1")
chromOverlap3.addData(Basic("chr1", 1300, 1400))
chromOverlap3.addData(Basic("chr1", 1400, 1800))
chromOverlap3.addData(Basic("chr1", 11000, 11200))
chromOverlapResult = chromOverlap1.getOverlapping(chromOverlap3)
print "Result Count: " + str(chromOverlapResult.count())
print "getOverlapCount: " + str(chromOverlap1.getOverlappingCount(chromOverlap3))
print "Some overlap:"
chromOverlap4 = Chrom("chr1")
chromOverlap4.addData(Basic("chr1", 100, 150))
chromOverlap4.addData(Basic("chr1", 400, 900))
chromOverlap4.addData(Basic("chr1", 11000, 11200))
chromOverlapResult = chromOverlap1.getOverlapping(chromOverlap4)
print "Result Count: " + str(chromOverlapResult.count())
print "getOverlapCount: " + str(chromOverlap1.getOverlappingCount(chromOverlap4))
print "All overlap: "
chromOverlap5 = Chrom("chr1")
chromOverlap5.addData(Basic("chr1", 100, 200))
chromOverlap5.addData(Basic("chr1", 400, 800))
chromOverlap5.addData(Basic("chr1", 1000, 1200))
chromOverlapResult = chromOverlap1.getOverlapping(chromOverlap5)
print "Result Count: " + str(chromOverlapResult.count())
print "getOverlapCount: " + str(chromOverlap1.getOverlappingCount(chromOverlap5))
