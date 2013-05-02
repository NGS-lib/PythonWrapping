#include <iostream>
#include "NGS++.h"

using namespace NGS;

extern "C" {
	uParser* New_parser(char* filename, char* type) {
		std::cout << "Before calling parser constructor" << std::endl;
		return new uParser(filename, type);
	}	
	bool eof(uParser* parser) {
		std::cout << "Before calling parser eof" << std::endl;
		return parser->eof();
	}
}
