from ctypes import *
import os
from uToken import uToken

class uWriter:

    def __init__(self,filename,typename):
        self.libNGS = cdll.LoadLibrary( os.environ.get('NGSWRAPPERLIB')  )
        if (filename!=""):
            self.obj = self.libNGS.new_Writer(filename,typename)
        else:
            self.obj = self.libNGS.new_cout_Writer(typename)

    def __del__(self):
    	self.libNGS.delete_Writer(self.obj)

    def write_token(self,token):
        self.libNGS.writeToken_writer(self.obj,token.obj)


    def write_string(self, text):
        self.libNGS.printString_Writer(self.obj,text)


if __name__=="__main__":
    from uParser_wrapper import uParser

    print "Loading a file, manually adjust to a local BAM file or will fail "
    bamParser = uParser("/home/local/USHERBROOKE/nora2001/Work/class/NGS_testing/data/BAM/H2AZ.bam","BAM")
    bed6writer = uWriter("","BED6")
    someToken = uToken()
    print "Get first entry and write to standard output in bed6"
    someToken = bamParser.get_next_entry()
    bed6writer.write_token(someToken)
    bed6writer = uWriter("current.txt","BED6")
    bed6writer =bamParser.get_next_entry()
    #while (A.eof()==0):
    #    C.write_token(A.get_next_entry())
       
    
