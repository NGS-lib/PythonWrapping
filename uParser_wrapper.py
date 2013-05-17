from ctypes import *
import os
libNGS = cdll.LoadLibrary(os.environ.get('NGSWRAPPERLIB'))

from uToken_wrapper import uToken

class uParser:

    def __init__(self,filename,typename):
        self.obj = libNGS.new_Parser(filename,typename)

    def __del__(self):
    	libNGS.delete_Parser(self.obj)

    def eof(self):
        return libNGS.eof_parser(self.obj)

    def get_next_entry(self):
        toReturn =uToken()
        toReturn.obj= libNGS.getNextEntry_parser(self.obj)
        return toReturn

    def get_previous_raw(self):
        libNGS.getPreviousRaw_parser.restype=c_char_p
        return libNGS.getPreviousRaw_parser(self.obj)

    def get_unformated_header(self):
        libNGS.getUnformatedHeader_parser.restype=c_char_p
        return libNGS.getUnformatedHeader_parser(self.obj)


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
    A = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/SAM/chr21_nucleosome_subset.sam","SAM")
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