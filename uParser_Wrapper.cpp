#include <iostream>
#include <string>
#include <vector>
#include "NGS/IO/Parser/uParser.h"

using namespace NGS;
using namespace std;

extern "C"{

    uParser* new_Parser(char* pFilename, char* pType){
            return new uParser(pFilename,pType);
    }

    void delete_Parser(uParser* pParser){
		delete pParser;
		pParser = NULL;
	}

    int eof_parser(uParser* pParser){

       // bool mytest;
       // std::cout<<pParser->eof()<<"\n";
       // mytest=pParser->eof();
        //std::cout<<mytest<<"\n";
        //return true;
        if (pParser->eof()==true)
            return 1;
        else
            return 0;
        //return pParser->eof();
    }
    uToken* getNextEntry_parser(uParser* pParser){

        uToken * token = new uToken;

        *token = (pParser->getNextEntry());
        return token;
    }

    char* getPreviousRaw_parser(uParser* pParser){
        std::string str;
        str=( pParser->getPreviousRaw() );
        char * writable = new char[str.size() + 1];
        std::copy(str.begin(), str.end(), writable);
        writable[str.size()] = '\0'; // don't forget the terminating 0
        return writable;
        };

    /** \brief Get an unformated version of header (i.e.: a single string containing the whole header)
    */
    char* getUnformatedHeader_parser(uParser* pParser)
     {
        std::string str;
        str=( pParser->getUnformatedHeader() );
        char * writable = new char[str.size() + 1];
        std::copy(str.begin(), str.end(), writable);
        writable[str.size()] = '\0'; // don't forget the terminating 0
        return writable;
     }
    /** \brief Get a specific data from header.
      */
   // std::string getHeaderParam(header_param name) const { return m_pParserBase->getHeaderParam(name); }
 //   std::vector<std::string> getHeaderParamVector(header_param name) const { return m_pParserBase->getHeaderParamVector(name); }
    /** \brief Check if there is a value associated with a given param.
      * \param header_param& name: name of the param to check.
      */
 //   bool isHeaderParamSet(const header_param& name) const { return m_pParserBase->isHeaderParamSet(name); }

}
