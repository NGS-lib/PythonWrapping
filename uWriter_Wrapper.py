from ctypes import *
stdc=cdll.LoadLibrary("libc.so.6")
stdcpp=cdll.LoadLibrary("libstdc++.so.6")
libNGS = cdll.LoadLibrary("/home/local/USHERBROOKE/nora2001/Work/libs/release/libpyThonWrap.so")

from uToken_wrapper import uToken

class uWriter:

    def __init__(self,filename,typename):
        self.obj = libNGS.new_Writer(filename,typename)

    def __del__(self):
    	libNGS.delete_Writer(self.obj)

    def write_token(self,token):
        libNGS.writeToken_writer(self.obj,token.obj)


    def write_string(self, text):
        libNGS.printString_Writer(self.obj,text)


if __name__=="__main__":
    from uParser_wrapper import uParser
    A = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/SAM/chr21_nucleosome_subset.sam","SAM")
    B = uToken()
    B = A.get_next_entry()
    C = uWriter("current.txt","BED6")
    while (A.eof()==0):
        C.write_token(A.get_next_entry())
    
    
