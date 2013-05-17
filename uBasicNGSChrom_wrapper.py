#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-08

from uBasicNGS_wrapper import *
import ctypes
from ctypes import *
lib = cdll.LoadLibrary('./libfoo.so')

class Chrom(object):
	def __init__(self, chromosomeName = None, chromosomeSize = None):
		if chromosomeName is None:
			self.obj = lib.New_basicChrom()
			if chromosomeSize is not None:
				self.setChrSize(chromosomeSize)
		elif chromosomeSize is None:
			self.obj = lib.New_basicChromName(chromosomeName)
		else:
			self.obj = lib.New_basicChromNameSize(chromosomeName, chromosomeSize)

	def __del__(self):
		lib.delete_basicChrom(self.obj)

	def getCopy(self):
		toReturn = Chrom()
		toReturn.obj = lib.getCopyChrom(self.obj)
		return toReturn

	def setChrSize(self, size):
		return lib.setChromSize(self.obj, size)

	def addData(self, basicNGS):
		lib.addData(self.obj, basicNGS.obj)

#	def addDataToken(self, token):
#		lib.addDataToken(self.obj, token.obj)

	def getChr(self):
		return c_char_p(lib.getChrChrom(self.obj)).value

	def getChromSize(self):
		return lib.getChromSize(self.obj)

	def count(self):
		return lib.countChrom(self.obj)

	def inferChrSize(self):
		return lib.inferChrSize(self.obj)

	def divideItemsIntoNBins(self, number, splitType="STRICT"):
		return lib.divideItemsIntoNBinsChrom(self.obj, number, splitType)

	def divideItemsIntoBinofSize(self, number, splitType="STRICT"):
		return lib.divideItemsIntoBinofSizeChrom(self.obj, number, splitType)

	def getSite(self, position):
		toReturn = Basic()
		toReturn.obj = lib.getSite(self.obj, position)
		return toReturn

	def avgSiteSize(self):
		return lib.avgSiteSize(self.obj)

	def minSiteSize(self):
		return lib.minSiteSize(self.obj)

	def maxSiteSize(self):
		return lib.maxSiteSize(self.obj)

	def sumSiteSize(self):
		return lib.sumSiteSize(self.obj)

#	def addRandomSites(self, size, count):
#		lib.addNRandomSite(self.obj, count)

	def count(self):
		return lib.count(self.obj)

	def getOverlapping(self, otherChrom, overlapType = "OVERLAP_PARTIAL"):
		toReturn = Chrom()
		toReturn.obj = lib.getOverlappingChrom(self.obj, otherChrom.obj, overlapType)
		return toReturn

#	def getOverlappingRegion(self, region, '

	def getOverlappingCount(self, otherChrom, overlapType = "OVERLAP_PARTIAL"):
		return lib.getOverlappingCount(self.obj, otherChrom.obj, overlapType)
