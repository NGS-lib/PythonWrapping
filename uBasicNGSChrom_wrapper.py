#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-05-08

import ctypes
from ctypes import *
lib = cdll.LoadLibrary('./libfoo.so')

class Chrom(object):
	def __init__(self, chromosomeName = None, chromosomeSize = None):
		if chromosomeName is None:
			self.obj = lib.New_basicChrom()
			if chromosomeSize is not None:
				lib.setChromSize(self.obj, chromosomeSize)
		elif chromosomeSize is None:
			self.obj = lib.New_basicChromName(chromosomeName)
		else:
			self.obj = lib.New_basicChromNameSize(chromosomeName, chromosomeSize)
