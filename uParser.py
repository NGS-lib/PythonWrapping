from ctypes import *
import os

from uToken import uToken

class uParser:

    def __init__(self,filename,typename):
        self.libNGS = cdll.LoadLibrary(os.environ.get('NGSWRAPPERLIB'))
        self.obj = self.libNGS.new_Parser(filename,typename)

    def __del__(self):
    	self.libNGS.delete_Parser(self.obj)

    def eof(self):
        return self.libNGS.eof_parser(self.obj)

    def get_next_entry(self):
        toReturn =uToken()
        toReturn.obj= self.libNGS.getNextEntry_parser(self.obj)
        return toReturn

    def get_previous_raw(self):
        self.libNGS.getPreviousRaw_parser.restype=c_char_p
        return self.libNGS.getPreviousRaw_parser(self.obj)

    def get_unformated_header(self):
        self.libNGS.getUnformatedHeader_parser.restype=c_char_p
        return self.libNGS.getUnformatedHeader_parser(self.obj)


if __name__=="__main__":
    A = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BED/bedH2AZ.bed","BED")
    B = uToken()
    B = A.get_next_entry()
    print A.eof()
    while (A.eof()==0):
        B = A.get_next_entry()
    print A.eof()
    
    if (B.is_param_set("CHR",0)):
        print (B.get_param("CHR",0))
    print A.get_previous_raw()
    print A.get_unformated_header()
    print "BAM"
    A = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BAM/H2AZ.bam","BAM")
    B = uToken()
    B = A.get_next_entry()
    print A.eof()
    Counter=0
    while (A.eof()==0):
        B = A.get_next_entry()
        Counter=Counter+1
        if (Counter%100000==0):
            print Counter
        if (Counter==300000):
            break
    print A.eof()
    
    if (B.is_param_set("CHR",0)):
        print (B.get_param("CHR",0))
    print A.get_previous_raw()
    print A.get_unformated_header()
