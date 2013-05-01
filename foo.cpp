#include <iostream>
#include "NGS++.h"

using namespace NGS;

extern "C" {
	uParser* New_parser(char* filename, char* type) {
		std::cout << "asdf" << std::endl;
		return new uParser(filename, type);
	}	
//	bool eof(uParser* parser) {
//		return parser->eof();
//	}
}
