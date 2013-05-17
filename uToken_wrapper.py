#!/usr/bin/python
# author: Alexei Nordell Markovits
# 2013-05-08


from ctypes import *
stdc=cdll.LoadLibrary("libc.so.6")
stdcpp=cdll.LoadLibrary("libstdc++.so.6")
libNGS = cdll.LoadLibrary("/home/local/USHERBROOKE/nora2001/Work/libs/release/libpyThonWrap.so")

class uToken:

    def __init__(self):
        self.obj = libNGS.new_token()

    def __del__(self):
    	libNGS.delete_token(self.obj)

    def print_token(self):
        libNGS.print_token(self.obj)

    def is_param_set(self, param, pos):
        return libNGS.isParamSet(self.obj,param, pos)
    def param_count(self, param):
        return libNGS.paramCount(self.obj,param)

    def get_param(self,param,pos):
    	libNGS.getParam.restype=c_char_p
    	return libNGS.getParam(self.obj,param,pos)

if __name__=="__main__":
	A = uToken()
	A.print_token()
	if (A.is_param_set("CHR",0)):
	    print("Yes!")
	else:
	    print("no")

	print ((A.param_count("CHR")))

