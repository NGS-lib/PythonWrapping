#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant & Alexei Nordell Markovits
# 2013-07-04

import ctypes
from ctypes import *
import os
from uParser_wrapper import *
from uWriter_Wrapper import *

class uBasic(object):
	def __init__(self, chr="", start=1, end=None, strand=None, score=None):
		self.NGSlib = cdll.LoadLibrary(os.environ.get('NGSWRAPPERLIB'))
		self.NGSlib.getScore.restype = ctypes.c_float
		if end is None:
			end = start
		if strand is None:
			strand = "FORWARD"
		self.obj = self.NGSlib.New_basic(chr, start, end, strand)
		if score is not None:
			self.NGSlib.setScore(self.obj, c_float(score))

	def __del__(self):
		self.NGSlib.delete_basic(self.obj)

	def get_chr(self):
		return c_char_p(self.NGSlib.getChrBasic(self.obj)).value

	def get_strand(self):
		return c_char_p(self.NGSlib.getStrand(self.obj)).value

	def get_start(self):
		return self.NGSlib.getStart(self.obj)

	def get_end(self):
		return self.NGSlib.getEnd(self.obj)

	def get_length(self):
		return self.NGSlib.getLength(self.obj)

	def get_score(self, position=None):
		self.NGSlib.getScore.restype = c_float
		if position is None:
			return self.NGSlib.getScore(self.obj)
		else:
			return self.NGSlib.getScorePosition(self.obj, position)

	def get_score_count(self):
		return self.NGSlib.getScoreCount(self.obj)

	def get_score_list(self):
		scoreList = []
		for i in range(0, self.get_score_count()):
			scoreList.append(self.get_score(i))
		return scoreList

	def is_reverse(self):
		return c_bool(self.NGSlib.isReverse(self.obj))

	def set_chr(self, chr):
		self.NGSlib.setChr(self.obj, chr)

	def set_strand(self, strand):
		self.NGSlib.setStrand(self.obj, strand)

	def set_start(self, start):
		self.NGSlib.setStart(self.obj, start)

	def set_end(self, end):
		self.NGSlib.setEnd(self.obj, end)

	def set_start_end(self, start, end):
		self.NGSlib.setStartEnd(self.obj, start, end)

	def set_score(self, score, position=None):
		if position is None:
			self.NGSlib.setScore(self.obj, c_float(score))
		else:
			self.NGSlib.setScorePosition(self.obj, c_float(score), position)

	def extend_site(self, extendLeft, extendRight=None):
		if extendRight is None:
			self.NGSlib.extendSite(self.obj, extendLeft)
		else:
			self.NGSlib.extendSiteLeftRight(self.obj, extendLeft, extendRight)

	def trim_site(self, trimLeft, trimRight=None):
		if trimRight is None:
			self.NGSlib.trimSite(self.obj, trimLeft)
		else:
			self.NGSlib.trimSiteLeftRight(self.obj, trimLeft, trimRight)

	def does_overlap(self, toCompare):
		return c_bool(self.NGSlib.doesOverlap(self.obj, toCompare.obj))

	def return_overlapping(self, toCompare):
		toReturn = uBasic()
		toReturn.obj = self.NGSlib.returnOverlapping(self.obj, toCompare.obj)
		return toReturn

	def return_merge(self, toCompare):
		toReturn = uBasic()
		toReturn.obj = self.NGSlib.returnMerge(self.obj, toCompare.obj)
		return toReturn

class uBasicChrom(object):
	def __init__(self, chromosomeName = None, chromosomeSize = None):
		self.lib = cdll.LoadLibrary(os.environ.get('NGSWRAPPERLIB'))
		if chromosomeName is None:
			self.obj = self.lib.New_basicChrom()
			if chromosomeSize is not None:
				self.set_chr_size(chromosomeSize)
		elif chromosomeSize is None:
			self.obj = self.lib.New_basicChromName(chromosomeName)
		else:
			self.obj = self.lib.New_basicChromNameSize(chromosomeName, chromosomeSize)

	def __del__(self):
		self.lib.delete_basicChrom(self.obj)

	def get_copy(self):
		toReturn = uBasicChrom()

		toReturn.obj = self.lib.getCopyChrom(self.obj)
		return toReturn

	def set_chr_size(self, size):
		self.lib.setChromSize(self.obj, size)

	def add_data(self, basicNGS):
		self.lib.addData(self.obj, basicNGS.obj)

#	def add_dataToken(self, token):
#		self.lib.addDataToken(self.obj, token.obj)

	def get_chr(self):
		return c_char_p(self.lib.getChrChrom(self.obj)).value

	def get_chrom_size(self):
		return self.lib.getChromSize(self.obj)

	def count(self):
		return self.lib.countChrom(self.obj)

	def infer_chr_size(self):
		return self.lib.inferChrSize(self.obj)

	def divide_items_into_n_bins(self, number, splitType="STRICT"):
		return self.lib.divideItemsIntoNBinsChrom(self.obj, number, splitType)

	def divide_items_into_bin_of_size(self, number, splitType="STRICT"):
		return self.lib.divideItemsIntoBinofSizeChrom(self.obj, number, splitType)

	def get_site(self, position):
		toReturn = uBasic()
		toReturn.obj = self.lib.getSite(self.obj, position)
		return toReturn

	def avg_site_size(self):
		return self.lib.avgSiteSize(self.obj)

	def min_site_size(self):
		return self.lib.minSiteSize(self.obj)

	def max_site_size(self):
		return self.lib.maxSiteSize(self.obj)

	def sum_site_size(self):
		return self.lib.sumSiteSize(self.obj)

	def add_random_sites(self, size, count, sigma=0):
		self.lib.addNRandomSite_Chrom(self.obj, size,count,sigma)

	def get_overlapping(self, otherChrom, overlapType = "OVERLAP_PARTIAL"):
		toReturn = uBasicChrom()
		toReturn.obj = self.lib.getOverlappingChrom(self.obj, otherChrom.obj, overlapType)
		return toReturn

	def get_overlapping_basic(self, region, overlapType = "OVERLAP_PARTIAL"):
		toReturn = uBasicChrom()
		toReturn.obj = self.lib.getOverlappingChromBasic(self.obj, region.obj, overlapType)
		return toReturn

	def get_overlapping_region(self, start, end, overlapType = "OVERLAP_PARTIAL"):
		toReturn = uBasicChrom()
		toReturn.obj = self.lib.getOverlappingChromRegion(self.obj, start, end, overlapType)
		return toReturn

	def get_not_overlapping(self, otherChrom, overlapType = "OVERLAP_PARTIAL"):
		toReturn = uBasicChrom()
		toReturn.obj = self.lib.getNotOverlapping(self.obj, otherChrom.obj, overlapType)
		return toReturn

	def get_overlapping_count(self, otherChrom, overlapType = "OVERLAP_PARTIAL"):
		return self.lib.getOverlappingCount(self.obj, otherChrom.obj, overlapType)

	def get_overlapping_count_basic(self, basic, overlapType = "OVERLAP_PARTIAL"):
		return self.lib.getOverlappingCountBasic(self.obj, basic.obj, overlapType)

	def get_overlapping_count_region(self, start, end, overlapType = "OVERLAP_PARTIAL"):
		return self.lib.getOverlappingCountRegion(self.obj, start, end, overlapType)

	def get_subset_count(self,start,end):
		return self.lib.getSubsetCount_basicChrom(self.obj, start, end)

	def get_subset(self, start, end):
		toReturn =uBasicChrom()
		toReturn.obj= self.lib.getSubset_basicChrom(self.obj, start, end)
		return toReturn
	def remove_subset(self, start, end):
		toReturn = uBasicChrom()
		toReturn.obj =self.lib.removeSubset_basicChrom(self.obj, start, end)
		return 
	def get_distinct(self,start,end):
		toReturn =uBasicChrom()
		toReturn.obj = self.lib.getDistinct_basicChrom(self.obj,start,end)
		return toReturn
	def remove_distinct(self,start,end):
		toReturn =uBasicChrom()
		toReturn.obj = self.lib.removeDistinct_basicChrom(self.obj,start,end)
		return toReturn

	def get_subsetCount(self, start, end):
		return self.lib.getSubsetCount_basicChrom(self.obj, start, end)

	def write_with_writer(self,writer):
		self.lib.writeWithWriter_Chrom(self.obj,writer.obj)

	def sort_sites(self):
		return self.lib.sortSites_basicChrom(self.obj)



class uBasicExp(object):

	def __init__(self):
		self.libNGS = cdll.LoadLibrary(os.environ.get('NGSWRAPPERLIB'))
		self.obj = self.libNGS.new_basicExperiment()

	def __del__(self):
		self.libNGS.delete_basicExperiment(self.obj)

	def is_chrom(self,chrom):
		self.libNGS.isChrom_basicExperiment.restype=ctypes.c_bool
		return self.libNGS.isChrom_basicExperiment(self.obj,chrom)

	def set_chr_size(self,chrom,size):
		self.libNGS.setChrSize_basicExperiment(self.obj,chrom,size)

	def get_chr_size(self,chrom):
		return self.libNGS.getChrSize_basicExperiment(self.obj,chrom)

	def removeChr(self,chrom):
		self.libNGS.removeChr_basicExperiment(self.obj,chrom)

	def count(self):
		return self.libNGS.count_basicExperiment(self.obj)

	def sort_sites(self):
		self.libNGS.sortSites_basicExperiment(self.obj)

	def is_sorted(self):
		self.libNGS.isSorted_basicExperiment.restype=ctypes.c_bool
		return self.libNGS.isSorted_basicExperiment(self.obj)

	def add_data_unit(self, data):
		self.libNGS.addDataUnit_basicExperiment(self.obj,data.obj)
	def add_data_chrom(self, data):
		self.libNGS.addDataChrom_basicExperiment(self.obj,data.obj)

	def load_with_parser(self, parser,count=0):
		self.libNGS.loadWithParser_basicExperiment(self.obj,parser.obj,count)

	def load_with_parser_path(self, path,type,count=0):
		self.libNGS.loadPathWithParser_basicExperiment(self.obj,path,type,count)

	def infer_chr_size(self):
		self.libNGS.inferChrSize_basicExperiment(self.obj)

	def write_with_writer(self, writer):
		self.libNGS.writeWithWriter_basicExperiment(self.obj, writer.obj)

	def get_site(self,chr,pos):
		toReturn =uBasic()
		toReturn.obj= self.libNGS.getSite_basicExperiment(self.obj,chr,pos)
		return toReturn

	def remove_site(self,chr,pos):
		self.libNGS.removeSite_basicExperiment(self.obj,chr,pos)

	def find_preceding_site(self,chr,pos):
		return self.libNGS.findPrecedingSitePos_basicExperiment(self.obj,chr,pos)
	
	def find_next_site(self,chr,pos):
		return self.libNGS.findNextSitePos_basicExperiment(self.obj,chr,pos)


	def get_subset_count(self,chr,start,end):
		return self.libNGS.getSubsetCount_region_basicExperiment(self.obj,chr,start,end)

	def get_subset(self,chr,start,end):
		toReturn = uBasicChrom()
		toReturn.obj= self.libNGS.getSubset_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def remove_subset(self,chr,start,end):
		toReturn =uBasicExp()
		toReturn.obj = self.libNGS.removeSubset_basicExperiment(self.obj,chr,start,end)
		return toReturn
#Second tests from here

	def get_overlapping_from_exp(self,exp):
		toReturn =uBasicExp()
		toReturn.obj = self.libNGS.getOverlapping_fromExp_basicExperiment(self.obj,exp.obj)
		return toReturn

	def get_overlapping_from_chrom(self,chrom):
		toReturn =uBasicExp()
		toReturn.obj = self.libNGS.getOverlapping_fromChrom_basicExperiment(self.obj,chrom)
		return toReturn

	def get_overlapping_from_region(self,chr, start, end):
		toReturn =uBasicExp()
		toReturn.obj = self.libNGS.getOverlapping_fromRegion_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def get_distinct(self,chr,start,end):
		toReturn =uBasicExp()
		toReturn.obj = self.libNGS.getDistinct_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def remove_distinct(self,chr,start,end):
		toReturn =uBasicExp()
		toReturn.obj = self.libNGS.removeDistinct_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def get_chr_count(self):
		return self.libNGS.getChrCount_basicExperiment(self.obj)








################TESTS###########################

def returnChromTests():
	
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	A = uBasicExp()
	A.load_with_parser(bedParser,5)
	achrom= get_subset
	
def firstTests():
	from uBasicNGS_wrapper import uBasic
	from uParser_wrapper import uParser
	from uWriter_Wrapper import uWriter
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	print "Make empty BasicExp"
	A = uBasicExp()
	A.sort_sites()
	B= uBasic("chr2",100,200)
	print "Test is Chrom"
	if (A.is_chrom("chr1")==0):
		print "Chrom check ok"
	else:
		print A.is_chrom("chr1")
	print "Test count"	
	print A.count()
	print "Test add Data"	
	A.add_data_unit(B)
	A.add_data_unit(uBasic("chr2",50,100))
	print A.count()
	if (A.is_chrom("chr2")==1):
		print "Chrom check2 ok"
	if (A.is_chrom("chr1")==1):
		print "Chrom check fail"
	
	print "before sort"
	print A.is_sorted()
	print "Test Sort"
	A.sort_sites()
	print "after sort"
	print A.is_sorted()
	print "Test Load With Parser"
	A.load_with_parser(bedParser,5)
	print A.count()
	A.load_with_parser_path("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED",3)
	print A.count()
	writer= uWriter("","BEDGRAPH")
	
	B= A.get_site("chr20",2)
	print B.get_chr(),B.get_start(),B.get_end()
	print A.count()
	A.removeChr("chr20")
	print A.count()
	A.write_with_writer(writer)
	A.sort_sites()
	C = A.find_preceding_site("chr2",0)
	print C
	C = A.find_next_site("chr2",600)
	print C
	print "----"
	A.remove_site("chr2",C)
	A.write_with_writer(writer)

	print "reloading"
	A.load_with_parser_path("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED",0)
	print "before subset"
	A.sort_sites()
	A.write_with_writer(writer)
	
	#F = BasicExp()

	A.remove_subset("chr2",30,120)
	print "after subset"
	A.write_with_writer(writer)

	print "before setSize"
	print A.get_chr_size("chr2")
	print "after setSize"
	A.set_chr_size("chr2",22999)
	print A.get_chr_size("chr2")
	print "after infer"
	A.infer_chr_size()
	print A.get_chr_size("chr2")

def secondTests():
	writer= uWriter("","BEDGRAPH")
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	A = uBasicExp()
	A.load_with_parser(bedParser,0)
	A.write_with_writer(writer)
	C = uBasicExp()
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	C.load_with_parser(bedParser,0)
	C.removeChr("chr2")
	C.write_with_writer
	print "before anything"
	A.write_with_writer(writer)
	L=A.get_overlapping_from_exp(C)
	print "after get overlapping exp"
	L.write_with_writer(writer)
	L=A.get_overlapping_from_region("chr20",257180,257480)
	print "after get overlapping region"
	L.write_with_writer(writer)
	#Need to test
	#get_overlapping_from_chrom(self,chrom):
	print "reset"
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	A = uBasicExp()
	A.load_with_parser(bedParser,0)
	A.write_with_writer(writer)

	print "after removeDistinct"
	A.sort_sites()
	A.remove_distinct("chr20",250000, 257700)
	A.write_with_writer(writer)
	print "reset"
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	A = uBasicExp()
	A.load_with_parser(bedParser,0)
	print "after getDistinct"
	A.sort_sites()
	F=A.get_distinct("chr20",250000, 257700)
	print F.count()
	F.write_with_writer(writer)
	print "ChrCount", F.get_chr_count()
	print "Get subset no chrom"
	print A.get_subset_count("chr22",250000, 257700)
	deleteA= uBasic()


def subsetTests():
	chrom = uBasicChrom()
	chrom.sort_sites()
	chrom.get_subset(1000,2000)
	print chrom.get_subset_count(1000,2000)
	chrom.get_subset(1000,2000)
	print "remove"
	chrom.remove_subset(1000, 2000)
	print "get"
	chrom.get_distinct(1000,2000)
	print "remove"
	chrom.remove_distinct(1000,2000)
	print "after"

def ManyTests():
	print "--------------------------"
	print "TESTS: uBasicNGSChrom"
	print "--------------------------"
	print "**** Tests for constructor"
	print "No param:"
	chrom = uBasicChrom()
	print "chr: " + chrom.get_chr()
	print "chrSize: " + str(chrom.get_chrom_size())
	print "Chrom Name"
	chromName = uBasicChrom("chr5")
	print "chr: " + chromName.get_chr()
	print "chrSize: " + str(chromName.get_chrom_size())
	print "Chrom Name Size:"
	chromNameSize = uBasicChrom("chr3", 123456)
	print "chr: " + chromNameSize.get_chr()
	print "chrSize: " + str(chromNameSize.get_chrom_size())
	print "Chrom Size:"
	chrom_size = uBasicChrom(chromosomeSize=123456)
	print "chr: " + chrom_size.get_chr()
	print "chrSize: " + str(chrom_size.get_chrom_size())

	print ""
	print "**** Tests for get_copy"
	chromCopy = chromNameSize.get_copy()
	print "chr: " + chromCopy.get_chr()
	print "chrSize: " + str(chromCopy.get_chrom_size())

	print ""
	print "**** Tests for add_data functions"
	chromAddData = uBasicChrom("chr3")
	basicAddData = uBasic("chr3", 100, 200)
	chromAddData.add_data(basicAddData)
	print "chr: " + chromAddData.get_chr()
	print "chrSize: " + str(chromAddData.get_chrom_size())

	print ""
	print "**** Tests for infer_chr_size "
	chromInfer = uBasicChrom("chr3")
	chromInfer.add_data(uBasic("chr3", 1000, 3000))
	print "chrSize (before): " + str(chromInfer.get_chrom_size())
	chromInfer.infer_chr_size()
	print "chrSize (after): " + str(chromInfer.get_chrom_size())
	chromInfer = uBasicChrom()
	print "chrSize (empty):" + str(chromInfer.get_chrom_size())

	print ""
	print "**** Tests for the divide_items_into_n_bins function"
	chromDivide = uBasicChrom("chr4")
	chromDivide.add_data(uBasic("chr4", 1000, 3000))
	print "count (before): " + str(chromDivide.count())
	chromDivide.divide_items_into_n_bins(10, "IGNORE")
	print "count (after): " + str(chromDivide.count())

	print ""
	print "**** Tests for the divideItemsIntoBinofSize function"
	chromDivide = uBasicChrom("chr4")
	chromDivide.add_data(uBasic("chr4", 1000, 2000))
	print "count (before): " + str(chromDivide.count())
	chromDivide.divide_items_into_bin_of_size(20, "IGNORE")
	print "count (after): " + str(chromDivide.count())

	print ""
	print "**** Tests for the function getSite"
	chromGetSite = uBasicChrom("chr1")
	chromGetSite.add_data(uBasic("chr1", 300, 500))
	aSite = chromGetSite.get_site(0)
	print "getSite: chr: " + aSite.get_chr()
	print "getSite: start: " + str(aSite.get_start())
	print "getSite: end: " + str(aSite.get_end())

	print ""
	print "**** Tests for the statistic functions"
	chromStats = uBasicChrom("chrX")
	chromStats.add_data(uBasic("chrX", 300, 500))
	chromStats.add_data(uBasic("chrX", 300, 600))
	chromStats.add_data(uBasic("chrX", 400, 500))
	print "avg: " + str(chromStats.avg_site_size())
	print "min: " + str(chromStats.min_site_size())
	print "max: " + str(chromStats.max_site_size())
	print "sum: " + str(chromStats.sum_site_size())
	print "count: " + str(chromStats.count())

	print "**** Tests for adding random sites"

	chromAddRandom = uBasicChrom("chrY")
	chromAddRandom.set_chr_size(100000)
	chromAddRandom.add_random_sites(100, 10,10)
	print "Count: " + str(chromAddRandom.count())
	writer= uWriter("","BEDGRAPH")
	chromAddRandom.write_with_writer(writer)
	print ""
	print "**** Tests for get_overlapping/get_overlapping_count (other Chrom)"
	chromOverlap1 = uBasicChrom("chr1")
	chromOverlap1.add_data(uBasic("chr1", 100, 200))
	chromOverlap1.add_data(uBasic("chr1", 400, 800))
	chromOverlap1.add_data(uBasic("chr1", 1000, 1200))
	print "Different chrom:"
	chromOverlap2 = uBasicChrom("chr2")
	chromOverlap2.add_data(uBasic("chr2", 100, 200))
	chromOverlap2.add_data(uBasic("chr2", 400, 800))
	chromOverlap2.add_data(uBasic("chr2", 1000, 1200))
	chromOverlapResult = chromOverlap1.get_overlapping(chromOverlap2)
	print "Result Count: " + str(chromOverlapResult.count())
	print "get_overlapCount: " + str(chromOverlap1.get_overlapping_count(chromOverlap2))
	print "No overlap:"
	chromOverlap3 = uBasicChrom("chr1")
	chromOverlap3.add_data(uBasic("chr1", 1300, 1400))
	chromOverlap3.add_data(uBasic("chr1", 1400, 1800))
	chromOverlap3.add_data(uBasic("chr1", 11000, 11200))
	chromOverlapResult = chromOverlap1.get_overlapping(chromOverlap3)
	print "Result Count: " + str(chromOverlapResult.count())
	print "get_overlapCount: " + str(chromOverlap1.get_overlapping_count(chromOverlap3))
	print "Some overlap:"
	chromOverlap4 = uBasicChrom("chr1")
	chromOverlap4.add_data(uBasic("chr1", 100, 150))
	chromOverlap4.add_data(uBasic("chr1", 400, 900))
	chromOverlap4.add_data(uBasic("chr1", 11000, 11200))
	chromOverlapResult = chromOverlap1.get_overlapping(chromOverlap4)
	print "Result Count: " + str(chromOverlapResult.count())
	print "get_overlapCount: " + str(chromOverlap1.get_overlapping_count(chromOverlap4))
	print "All overlap: "
	chromOverlap5 = uBasicChrom("chr1")
	chromOverlap5.add_data(uBasic("chr1", 100, 200))
	chromOverlap5.add_data(uBasic("chr1", 400, 800))
	chromOverlap5.add_data(uBasic("chr1", 1000, 1200))
	chromOverlapResult = chromOverlap1.get_overlapping(chromOverlap5)
	print "Result Count: " + str(chromOverlapResult.count())
	print "get_overlapCount: " + str(chromOverlap1.get_overlapping_count(chromOverlap5))

	print ""
	print "**** Tests for get_overlapping/get_overlapping_count (basic)"
	chromBasicOverlap1 = uBasicChrom("chr2")
	chromBasicOverlap1.add_data(uBasic("chr2", 100, 200))
	chromBasicOverlap1.add_data(uBasic("chr2", 400, 800))
	chromBasicOverlap1.add_data(uBasic("chr2", 1000, 1200))
	print "chromBasicOverlap1.count(): " + str(chromBasicOverlap1.count())
	basicOverlap = uBasic("chr2", 50, 900)
	chromOverlapResult = chromBasicOverlap1.get_overlapping_basic(basicOverlap)
	print "Result Count: " + str(chromOverlapResult.count())
	print "get_overlapCount: " + str(chromBasicOverlap1.get_overlapping_count_basic(basicOverlap))
	aSite = chromOverlapResult.get_site(0)
	print "get_site: chr: " + aSite.get_chr()
	print "get_site: start: " + str(aSite.get_start())
	print "get_site: end: " + str(aSite.get_end())

	print ""
	print "**** Tests for get_overlapping/get_overlapping_count (region)"
	chromRegionOverlap1 = uBasicChrom("chr3")
	chromRegionOverlap1.add_data(uBasic("chr3", 100, 200))
	chromRegionOverlap1.add_data(uBasic("chr3", 400, 800))
	chromRegionOverlap1.add_data(uBasic("chr3", 1000, 1200))
	chromOverlapResult = chromRegionOverlap1.get_overlapping_region(50, 900)
	print "Result Count: " + str(chromOverlapResult.count())
	print "get_overlapCount: " + str(chromBasicOverlap1.get_overlapping_count_region(50, 900))

	print ""
	print "**** Tests for get_not_overlapping (other Chrom)"
	chromNotOverlap1 = uBasicChrom("chr1")
	chromNotOverlap1.add_data(uBasic("chr1", 100, 200))
	chromNotOverlap1.add_data(uBasic("chr1", 400, 800))
	chromNotOverlap1.add_data(uBasic("chr1", 1000, 1200))
	print "Different chrom:"
	chromNotOverlap2 = uBasicChrom("chr2")
	chromNotOverlap2.add_data(uBasic("chr2", 100, 200))
	chromNotOverlap2.add_data(uBasic("chr2", 400, 800))
	chromNotOverlap2.add_data(uBasic("chr2", 1000, 1200))
	chromNotOverlapResult = chromNotOverlap1.get_not_overlapping(chromNotOverlap2)
	print "Result Count: " + str(chromNotOverlapResult.count())
#	print "get_not_overlapCount: " + str(chromNotOverlap1.get_not_overlapping_count(chromNotOverlap2))
	print "No overlap:"
	chromNotOverlap3 = uBasicChrom("chr1")
	chromNotOverlap3.add_data(uBasic("chr1", 1300, 1400))
	chromNotOverlap3.add_data(uBasic("chr1", 1400, 1800))
	chromNotOverlap3.add_data(uBasic("chr1", 11000, 11200))
	chromNotOverlapResult = chromNotOverlap1.get_not_overlapping(chromNotOverlap3)
	print "Result Count: " + str(chromNotOverlapResult.count())
#	print "get_not_overlapCount: " + str(chromNotOverlap1.get_not_overlapping_count(chromNotOverlap3))
	print "Some overlap:"
	chromNotOverlap4 = uBasicChrom("chr1")
	chromNotOverlap4.add_data(uBasic("chr1", 100, 150))
	chromNotOverlap4.add_data(uBasic("chr1", 400, 900))
	chromNotOverlap4.add_data(uBasic("chr1", 11000, 11200))
	chromNotOverlapResult = chromNotOverlap1.get_not_overlapping(chromNotOverlap4)
	print "Result Count: " + str(chromNotOverlapResult.count())
#	print "get_overlapCount: " + str(chromNotOverlap1.get_not_overlapping_count(chromNotOverlap4))
	print "All overlap: "
	chromNotOverlap5 = uBasicChrom("chr1")
	chromNotOverlap5.add_data(uBasic("chr1", 100, 200))
	chromNotOverlap5.add_data(uBasic("chr1", 400, 800))
	chromNotOverlap5.add_data(uBasic("chr1", 1000, 1200))
	chromNotOverlapResult = chromNotOverlap1.get_not_overlapping(chromNotOverlap5)
	print "Result Count: " + str(chromNotOverlapResult.count())
#	print "get_not_overlapCount: " + str(chromNotOverlap1.get_not_overlapping_count(chromNotOverlap5))


def ubasic_tests():
	# Tests with the uBasicNGS
	print "**** Tests constructor basic"
	b = uBasic()
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor chr"
	b = uBasic("chr1")
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor start"
	b = uBasic("chr1", 1000)
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor end"
	b = uBasic("chr1", 1000, 1200)
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor strand"
	b = uBasic("chr1", 1000, 1200, "-")
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "**** Tests constructor score"
	b = uBasic("chr1", 1000, 1200, "-", 2.4)
	print "Chr: " + b.get_chr()
	print "Start: " + str(b.get_start())
	print "End: " + str(b.get_end())
	print "Strand: " + str(b.get_strand())
	print "Score: " + str(b.get_score())

	print "**** Misc tests"
	b = uBasic("chr1", 100, 200)
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
	b2 = uBasic("chr2", 100, 200)
	b3 = uBasic("chr2", 201, 300)
	b4 = uBasic("chr1", 100, 200)
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



if __name__=="__main__":
	ubasic_tests()
	subsetTests()
	ManyTests()
	firstTests()
	secondTests()
	
