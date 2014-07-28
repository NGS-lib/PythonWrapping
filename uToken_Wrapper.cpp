#include <iostream>
#include <string>
#include <vector>
#include "NGS/IO/uToken.h"

using namespace NGS;
using namespace std;

extern "C"{
    uToken* new_token(){return new uToken();}
    void print_token(uToken* pToken) {
		(pToken->print(std::cout));

	}
	void delete_token(uToken* pToken){
		delete pToken;
		//pToken = NULL;
	}

    bool isParamSet(uToken* pToken, char* pParam, int pPos)
    {
      return pToken->isParamSet(pToken->convertStringToTokenParam(pParam),pPos);
    }

     int paramCount(uToken* pToken, char* pParam){
         return pToken->paramCount(pToken->convertStringToTokenParam(pParam));
     }

    //This might leak, validate.
    char* getParam(uToken* pToken, char* pParam, int pPos){
        std::string str;
        str=( pToken->getParam(pToken->convertStringToTokenParam(pParam),pPos) );

        //char * writable = new char[str.size() + 1];
        char *writable = static_cast<char *>(malloc(sizeof(char) * ( str.size() + 1 )));
        std::copy(str.begin(), str.end(), writable);
        writable[str.size()] = '\0'; // don't forget the terminating 0
        return writable;
    }


    void free_char(char* char_array){
        //std::cout<<"HIHIHIHIHIHIHIHI\n";
         //   free(char_array);
        }

}



