#include <iostream>
#include <string>
#include <vector>
#include "NGS/IO/Writer/uWriter.h"

using namespace NGS;
using namespace std;

extern "C"{


     uWriter* new_cout_Writer(char* pType){
            return new uWriter(&std::cout,pType);
    }


    uWriter* new_Writer(char* pFilename, char* pType){
            return new uWriter(pFilename,pType);
    }

    void delete_Writer(uWriter* uWriter){
		delete uWriter;
		uWriter = NULL;
	}

    void writeToken_writer(uWriter* pWriter, uToken* pToken){
        pWriter->writeToken(*pToken);
    }

    void printString_Writer(uWriter* pWriter, char * pToWrite){
        pWriter->printString(pToWrite);
        };

}
