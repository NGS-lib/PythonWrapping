#!/usr/bin/python
# author: Alexei Nordell
# 2013-05-08

import ctypes
from ctypes import *
import os
libNGS = cdll.LoadLibrary(os.environ.get('NGSWRAPPERLIB'))
from uBasicNGS_wrapper import Basic
from uParser_wrapper import uParser
from uWriter_Wrapper import uWriter

class BasicExp(object):

	def __init__(self):
		self.obj = libNGS.new_basicExperiment()

	def __del__(self):
		libNGS.delete_basicExperiment(self.obj)

	def is_chrom(self,chrom):
		libNGS.isChrom_basicExperiment.restype=ctypes.c_bool
		return libNGS.isChrom_basicExperiment(self.obj,chrom)

	def set_chr_size(self,chrom,size):
		libNGS.setChrSize_basicExperiment(self.obj,chrom,size)

	def get_chr_size(self,chrom):
		return libNGS.getChrSize_basicExperiment(self.obj,chrom)

	def removeChr(self,chrom):
		libNGS.removeChr_basicExperiment(self.obj,chrom)

	def count(self):
		return libNGS.count_basicExperiment(self.obj)

	def sort_sites(self):
		libNGS.sortSites_basicExperiment(self.obj)

	def is_sorted(self):
		libNGS.isSorted_basicExperiment.restype=ctypes.c_bool
		return libNGS.isSorted_basicExperiment(self.obj)

	def add_data_unit(self, data):
		libNGS.addDataUnit_basicExperiment(self.obj,data.obj)
	def add_data_chrom(self, data):
		libNGS.addDataChrom_basicExperiment(self.obj,data.obj)

	def load_with_parser(self, parser,count):
		libNGS.loadWithParser_basicExperiment(self.obj,parser.obj,count)

	def load_with_parser_path(self, path,type,count):
		libNGS.loadPathWithParser_basicExperiment(self.obj,path,type,count)

	def infer_chr_size(self):
		libNGS.inferChrSize_basicExperiment(self.obj)

	def write_with_writer(self, writer):
		libNGS.writeWithWriter_basicExperiment(self.obj, writer.obj)

	def get_site(self,chr,pos):
		toReturn =Basic()
		toReturn.obj= libNGS.getSite_basicExperiment(self.obj,chr,pos)
		return toReturn

	def remove_site(self,chr,pos):
		libNGS.removeSite_basicExperiment(self.obj,chr,pos)

	def find_preceding_site(self,chr,pos):
		return libNGS.findPrecedingSitePos_basicExperiment(self.obj,chr,pos)
	
	def find_next_site(self,chr,pos):
		return libNGS.findNextSitePos_basicExperiment(self.obj,chr,pos)


	def get_subset_count(self,chr,start,end):
		return libNGS.getSubsetCount_region_basicExperiment(self.obj,chr,start,end)

	def get_subset(self,chr,start,end):
		#toReturn =()
		#toReturn.obj= libNGS.getSubset_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def remove_subset(self,chr,start,end):
		toReturn =BasicExp()
		toReturn.obj = libNGS.removeSubset_basicExperiment(self.obj,chr,start,end)
		return toReturn
#Second tests from here

	def get_overlapping_from_exp(self,exp):
		toReturn =BasicExp()
		toReturn.obj = libNGS.getOverlapping_fromExp_basicExperiment(self.obj,exp.obj)
		return toReturn

	def get_overlapping_from_chrom(self,chrom):
		toReturn =BasicExp()
		toReturn.obj = libNGS.getOverlapping_fromChrom_basicExperiment(self.obj,chrom)
		return toReturn

	def get_overlapping_from_region(self,chr, start, end):
		toReturn =BasicExp()
		toReturn.obj = libNGS.getOverlapping_fromRegion_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def get_distinct(self,chr,start,end):
		toReturn =BasicExp()
		toReturn.obj = libNGS.getDistinct_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def remove_distinct(self,chr,start,end):
		toReturn =BasicExp()
		toReturn.obj = libNGS.removeDistinct_basicExperiment(self.obj,chr,start,end)
		return toReturn

	def get_chr_count(self):
		return libNGS.getChrCount_basicExperiment(self.obj)


def firstTests():
	from uBasicNGS_wrapper import Basic
	from uParser_wrapper import uParser
	from uWriter_Wrapper import uWriter
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	print "Make empty BasicExp"
	A = BasicExp()

	B= Basic("chr2",100,200)
	print "Test is Chrom"
	if (A.is_chrom("chr1")==0):
		print "Chrom check ok"
	else:
		print A.is_chrom("chr1")
	print "Test count"	
	print A.count()
	print "Test add Data"	
	A.add_data_unit(B)
	A.add_data_unit(Basic("chr2",50,100))
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
	print B.getChr(),B.getStart(),B.getEnd()
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
	from uBasicNGS_wrapper import Basic
	from uParser_wrapper import uParser
	from uWriter_Wrapper import uWriter
	writer= uWriter("","BEDGRAPH")
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	A = BasicExp()
	A.load_with_parser(bedParser,0)
	A.write_with_writer(writer)
	C = BasicExp()
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
	A = BasicExp()
	A.load_with_parser(bedParser,0)
	A.write_with_writer(writer)

	print "after removeDistinct"
	A.sort_sites()
	A.remove_distinct("chr20",250000, 257700)
	A.write_with_writer(writer)
	print "reset"
	bedParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
	A = BasicExp()
	A.load_with_parser(bedParser,0)
	print "after getDistinct"
	A.sort_sites()
	F=A.get_distinct("chr20",250000, 257700)
	print F.count()
	F.write_with_writer(writer)
	print "ChrCount", F.get_chr_count()
	print A.get_subset_count("chr22",250000, 257700)

if __name__=="__main__":
	#firstTests()
	secondTests()
	
