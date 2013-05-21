#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-08

from uBasicNGS_wrapper import *
from uWriter_Wrapper import *
from ctypes import *
import os


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
		return self.lib.setChromSize(self.obj, size)

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

	def count(self):
		return self.lib.count(self.obj)

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
if __name__=="__main__":
	subsetTests()



