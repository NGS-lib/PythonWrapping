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
		cout << "Before calling uBasicNGS->getChr()" << endl;
		return (char*) (basic->getChr().c_str());
	}

	char* getStrand(uBasicNGS* basic) {
		cout << "Before calling uBasicNGS->getStrand()" << endl;
		if (basic->getStrand() == StrandDir::FORWARD) {
			string strand_string("FORWARD");
			return (char*)(strand_string.c_str());
		}
		else {
			string strand_string("REVERSE");
			return (char*)(strand_string.c_str());
		}
	}

	long int getStart(uBasicNGS* basic) {
		cout << "Before calling uBasicNGS->getStart()" << endl;
		return basic->getStart();
	}

	long int getEnd(uBasicNGS* basic) {
		cout << "Before calling uBasicNGS->getEnd()" << endl;
		return basic->getEnd();
	}

	long int getLength(uBasicNGS* basic) {
		cout << "Before calling uBasicNGS->getLength()" << endl;
		return basic->getLength();
	}

	float getScore(uBasicNGS* basic) {
		cout << "Before calling uBasicNGS->getScore" << endl;
		return basic->getScore();
	}

	float getScorePosition(uBasicNGS* basic, int position) {
		cout << "Before calling uBasicNGS->getScore (position)" << endl;
		return basic->getScore(position);
	}

	int getScoreCount(uBasicNGS* basic) {
		cout << "Before calling uBasicNGS->getScoreCount" << endl;
		return basic->getScoreCount();
	}

	bool isReverse(uBasicNGS* basic) {
		cout << "Before calling uBasicNGS->isReverse" << endl;
		return basic->isReverse();
	}

	void setChr(uBasicNGS* basic, char* chr) {
		cout << "Before calling uBasicNGS->setChr()" << endl;
		basic->setChr(chr);
	}

	void setStrand(uBasicNGS* basic, char* strand) {
		cout << "Before calling uBasicNGS constructor" << endl;
		string strand_string(strand);
		if (strand_string == "+" || strand_string == "forward" || strand_string == "FORWARD") {
			basic->setStrand(StrandDir::FORWARD);
		}
		else if (strand_string == "-" || strand_string == "reverse" || strand_string == "REVERSE") {
			basic->setStrand(StrandDir::REVERSE);
		}
		else {
			throw logic_error("Invalid strand type");
		}
	}

	void setStart(uBasicNGS* basic, long int start) {
		cout << "Before calling uBasicNGS setStart" << endl;
		basic->setStart(start);
	}

	void setEnd(uBasicNGS* basic, long int end) {
		cout << "Before calling uBasicNGS setEnd" << endl;
		basic->setEnd(end);
	}

	void setStartEnd(uBasicNGS* basic, long int start, long int end) {
		cout << "Before calling uBasicNGS setStartEnd" << endl;
		basic->setStartEnd(start, end);
	}

	void setScore(uBasicNGS* basic, float score) {
		cout << "Before calling uBasicNGS setScore" << endl;
		basic->setScore(score);
	}

	void setScorePosition(uBasicNGS* basic, float score, int position) {
		cout << "Before calling uBasicNGS setScore (position)" << endl;
		basic->setScore(score, position);
	}

	void extendSite(uBasicNGS* basic, long int extend) {
		cout << "Before calling uBasicNGS extendSite" << endl;
		basic->extendSite(extend);
	}

	void extendSiteLeftRight(uBasicNGS* basic, long int extendLeft, long int extendRight) {
		cout << "Before calling uBasicNGS extendSite (left, right)" << endl;
		basic->extendSite(extendLeft, extendRight);
	}

	void trimSite(uBasicNGS* basic, long int trim) {
		cout << "Before calling uBasicNGS trimSite" << endl;
		basic->trimSite(trim);
	}

	void trimSiteLeftRight(uBasicNGS* basic, long int trimLeft, long int trimRight) {
		cout << "Before calling uBasicNGS trimSite (left, right)" << endl;
		basic->trimSite(trimLeft, trimRight);
	}

} // End of extern "C"
