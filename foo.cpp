#include <iostream>
#include <string>
#include <vector>
#include "NGS++.h"

using namespace NGS;
using namespace std;

extern "C" {
	/* Tests with parser */
	uParser* New_parser(char* filename, char* type) {
		return new uParser(filename, type);
	}	

	bool eof(uParser* parser) {
		return parser->eof();
	}
} // End of extern "C"
