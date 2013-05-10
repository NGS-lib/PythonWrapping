#include "NGS++.h"

using namespace NGS;
using namespace std;

extern "C" {
	/** Constructors / Destructor */
	uBasicNGSChrom* New_basicChrom() {
		return new uBasicNGSChrom();
	}

	uBasicNGSChrom* New_basicChromName(char* chrName) {
		return new uBasicNGSChrom(chrName);
	}

	uBasicNGSChrom* New_basicChromNameSize(char* chrName, long long int chrSize) {
		return new uBasicNGSChrom(chrName, chrSize);
	}

	void delete_basicChrom(uBasicNGSChrom* chrom) {
		delete chrom;
		chrom = NULL;
	}

	/** Setters / Adders*/
	void setChromSize(uBasicNGSChrom* chrom, long long int size) {
		chrom->setChromSize(size);
	}

	void addData(uBasicNGSChrom* chrom, uBasicNGS* basic) {
		chrom->addData(*basic);
	}

	/** Getters */
	uBasicNGSChrom* getCopyChrom(uBasicNGSChrom* chrom) {
		return new uBasicNGSChrom(*chrom);
	}

	char* getChrChrom(uBasicNGSChrom* chrom) {
		if (chrom->getChr() == "") {
			string toReturn(" ");
			return (char*)(toReturn.c_str());
		}
		return (char*) (chrom->getChr().c_str());
	}

	long long int getChromSize(uBasicNGSChrom* chrom) {
		return chrom->getChromSize();
	}

	void inferChrSize(uBasicNGSChrom* chrom) {
		chrom->inferChrSize();
	}

	long int countChrom(uBasicNGSChrom* chrom) {
		return chrom->count();
	}
	/* Misc */
	void divideItemsIntoNBinsChrom(uBasicNGSChrom* chrom, int number, char* splitType) {
		string splitTypeString(splitType);
		if (splitTypeString == "STRICT") {
			chrom->divideItemsIntoNBins(number, SplitType::STRICT);
		}
		else if (splitTypeString == "IGNORE") {
			chrom->divideItemsIntoNBins(number, SplitType::IGNORE);
		}
		else if (splitTypeString == "EXTEND") {
			chrom->divideItemsIntoNBins(number, SplitType::EXTEND);
		}
		else if (splitTypeString == "ADD") {
			chrom->divideItemsIntoNBins(number, SplitType::ADD);
		}
		else {
			throw runtime_error("divideItemsIntoNBinsChrom: Invalid splitType (" + splitTypeString + ")");
		}
	}
} // End of extern "C"
