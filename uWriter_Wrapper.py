from ctypes import *
import os
from uToken_wrapper import uToken

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

    samParser = uParser("data/sample.sam","SAM")
    bed6writer = uWriter("","BED6")
    someToken = uToken()
    print "Get first entry and write to standard output in bed6 to current.txt"
    someToken = samParser.get_next_entry()
    bed6writer.write_token(someToken)
    bed6writer = uWriter("current.txt","BED6")
    bed6writer.write_token(samParser.get_next_entry())

       
    
