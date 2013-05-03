#include <iostream>
#include <string>
#include "NGS++.h"

using namespace NGS;
using namespace std;

extern "C" {
	/* Tests with parser */
	uParser* New_parser(char* filename, char* type) {
		cout << "Before calling parser constructor" << endl;
		return new uParser(filename, type);
	}	

	bool eof(uParser* parser) {
		cout << "Before calling parser eof" << endl;
		return parser->eof();
	}

	/* Tests with uBasicNGS */
	uBasicNGS* New_basic(char* chr, long long int start, long long int end, char* strand) {
		cout << "Before calling uBasicNGS constructor" << endl;
		string strand_string(strand);
		if (strand_string == "+" || strand_string == "forward" || strand_string == "FORWARD") {
			return new uBasicNGS(chr, start, end, StrandDir::FORWARD);
		}
		else if (strand_string == "-" || strand_string == "reverse" || strand_string == "REVERSE") {
			return new uBasicNGS(chr, start, end, StrandDir::REVERSE);
		}
		else {
			throw logic_error("Invalid strand type");
		}
	}

	char* getChr(uBasicNGS* basic) {
		return (char*) (basic->getChr().c_str());
	}
} // End of extern "C"
