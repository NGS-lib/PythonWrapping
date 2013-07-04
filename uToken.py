#!/usr/bin/python
# author: Alexei Nordell Markovits
# 2013-05-08


from ctypes import *
import os

class uToken:
    def __init__(self):
	self.libNGS = cdll.LoadLibrary(os.environ.get('NGSWRAPPERLIB'))
        self.obj = self.libNGS.new_token()

    def __del__(self):
    	self.libNGS.delete_token(self.obj)

    def print_token(self):
        self.libNGS.print_token(self.obj)

    def is_param_set(self, param, pos=0):
        return self.libNGS.isParamSet(self.obj,param, pos)
    def param_count(self, param):
        return self.libNGS.paramCount(self.obj,param)

    def get_param(self,param,pos=0):
    	self.libNGS.getParam.restype=c_char_p
    	return self.libNGS.getParam(self.obj,param,pos)

if __name__=="__main__":
	A = uToken()
	A.print_token()
	if (A.is_param_set("CHR",0)):
	    print("Yes!")
	else:
	    print("no")

	print ((A.param_count("CHR")))

