#!/usr/bin/python
# author: Alexei Nordell
# 2013-05-08

import ctypes
from ctypes import *
import os

from uBasicNGS_wrapper import *
from uBasicNGSChrom_wrapper import *
from uParser_wrapper import *
from uWriter_Wrapper import *

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



def returnChromTests():
	#not finished
	bedParser = uParser("data/sample.bed","BED")
	A = uBasicExp()
	A.load_with_parser(bedParser,5)
	#achrom= get_subset
	

def firstTests():
	from uBasicNGS_wrapper import uBasic
	from uParser_wrapper import uParser
	from uWriter_Wrapper import uWriter
	bedParser = uParser("data/sample.bed","BED")
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
	A.load_with_parser_path("data/sample.bed","BED",3)
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
	A.load_with_parser_path("data/sample.bed","BED",0)
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
	bedParser = uParser("data/sample.bed","BED")
	A = uBasicExp()
	A.load_with_parser(bedParser,0)
	A.write_with_writer(writer)
	C = uBasicExp()
	bedParser = uParser("data/sample.bed","BED")
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
	bedParser = uParser("data/sample.bed","BED")
	A = uBasicExp()
	A.load_with_parser(bedParser,0)
	A.write_with_writer(writer)

	print "after removeDistinct"
	A.sort_sites()
	A.remove_distinct("chr20",250000, 257700)
	A.write_with_writer(writer)
	print "reset"
	bedParser = uParser("data/sample.bed","BED")
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
if __name__=="__main__":
	firstTests()
	secondTests()
	
