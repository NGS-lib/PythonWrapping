#include <iostream>
#include <string>
#include <vector>
#include "NGS++.h"

using namespace NGS;
using namespace std;

extern "C" {
	uBasicNGS* New_basic(char* chr, long long int start, long long int end, char* strand) {
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

	void delete_basic(uBasicNGS* basic) {
		delete basic;
		basic = NULL;
	}

	char* getChr(uBasicNGS* basic) {
		return (char*) (basic->getChr().c_str());
	}

	char* getStrand(uBasicNGS* basic) {
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
		return basic->getStart();
	}

	long int getEnd(uBasicNGS* basic) {
		return basic->getEnd();
	}

	long int getLength(uBasicNGS* basic) {
		return basic->getLength();
	}

	float getScore(uBasicNGS* basic) {
		return basic->getScore();
	}

	float getScorePosition(uBasicNGS* basic, int position) {
		return basic->getScore(position);
	}

	int getScoreCount(uBasicNGS* basic) {
		return basic->getScoreCount();
	}

	bool isReverse(uBasicNGS* basic) {
		return basic->isReverse();
	}

	void setChr(uBasicNGS* basic, char* chr) {
		basic->setChr(chr);
	}

	void setStrand(uBasicNGS* basic, char* strand) {
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
		basic->setStart(start);
	}

	void setEnd(uBasicNGS* basic, long int end) {
		basic->setEnd(end);
	}

	void setStartEnd(uBasicNGS* basic, long int start, long int end) {
		basic->setStartEnd(start, end);
	}

	void setScore(uBasicNGS* basic, float score) {
		basic->setScore(score);
	}

	void setScorePosition(uBasicNGS* basic, float score, int position) {
		basic->setScore(score, position);
	}

	void extendSite(uBasicNGS* basic, long int extend) {
		basic->extendSite(extend);
	}

	void extendSiteLeftRight(uBasicNGS* basic, long int extendLeft, long int extendRight) {
		basic->extendSite(extendLeft, extendRight);
	}

	void trimSite(uBasicNGS* basic, long int trim) {
		basic->trimSite(trim);
	}

	void trimSiteLeftRight(uBasicNGS* basic, long int trimLeft, long int trimRight) {
		basic->trimSite(trimLeft, trimRight);
	}

	bool doesOverlap(uBasicNGS* basic, uBasicNGS* toCompare) {
		return basic->doesOverlap(*toCompare);
	}

	uBasicNGS* returnOverlapping(uBasicNGS* basic, uBasicNGS* toCompare) {
		return new uBasicNGS(basic->returnOverlapping(*toCompare));
	}

	uBasicNGS* returnMerge(uBasicNGS* basic, uBasicNGS* toCompare) {
		return new uBasicNGS(basic->returnMerge(*toCompare));
	}

} // End of extern "C"
