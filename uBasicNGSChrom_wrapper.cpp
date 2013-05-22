#include "NGS++.h"
#include <random>

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

	void delete_basicChrom(uBasicNGSChrom* chrom){
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

	uBasicNGS* getSite(uBasicNGSChrom* chrom, long long position) {
		return new uBasicNGS(chrom->getSite(position));
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
	void divideItemsIntoBinofSizeChrom(uBasicNGSChrom* chrom, int number, char* splitType) {
		string splitTypeString(splitType);
		if (splitTypeString == "STRICT") {
			chrom->divideItemsIntoBinofSize(number, SplitType::STRICT);
		}
		else if (splitTypeString == "IGNORE") {
			chrom->divideItemsIntoBinofSize(number, SplitType::IGNORE);
		}
		else if (splitTypeString == "EXTEND") {
			chrom->divideItemsIntoBinofSize(number, SplitType::EXTEND);
		}
		else if (splitTypeString == "ADD") {
			chrom->divideItemsIntoBinofSize(number, SplitType::ADD);
		}
		else {
			throw runtime_error("divideItemsIntoBinofSizeChrom: Invalid splitType (" + splitTypeString + ")");
		}
	}
	unsigned long long avgSiteSize(uBasicNGSChrom* chrom) {
		return chrom->avgSiteSize();
	}
	unsigned long long minSiteSize(uBasicNGSChrom* chrom) {
		return chrom->minSiteSize();
	}
	unsigned long long maxSiteSize(uBasicNGSChrom* chrom) {
		return chrom->maxSiteSize();
	}
	unsigned long long sumSiteSize(uBasicNGSChrom* chrom) {
		return chrom->sumSiteSize();
	}
	// This throw a param_throw for some reason...
	void addNRandomSite_Chrom(uBasicNGSChrom* chrom, int size, int count, int sigma) {
		std::random_device rd;
		std::mt19937 gen(rd());
		chrom->addNRandomSite(size, count, gen, sigma);
	}

	void writeWithWriter_Chrom(uBasicNGSChrom* chrom,uWriter* pWriter){
        chrom->writeWithWriter(*pWriter);
	}

	long int count(uBasicNGSChrom* chrom) {
		return chrom->count();
	}
	uBasicNGSChrom* getOverlappingChrom(uBasicNGSChrom* chrom, uBasicNGSChrom* otherChrom, char* overlapType) {
		string overlapTypeString(overlapType);
		if (overlapTypeString == "OVERLAP_PARTIAL") {
			return new uBasicNGSChrom(chrom->getOverlapping(*otherChrom, OverlapType::OVERLAP_PARTIAL));
		}
		else if (overlapTypeString == "OVERLAP_COMPLETE") {
			return new uBasicNGSChrom(chrom->getOverlapping(*otherChrom, OverlapType::OVERLAP_COMPLETE));
		}
		else if (overlapTypeString == "OVERLAP_CENTER") {
			return new uBasicNGSChrom(chrom->getOverlapping(*otherChrom, OverlapType::OVERLAP_CENTER));
		}
		else {
			throw runtime_error("getOverlapping: Invalid overlapType(" + overlapTypeString + ")");
		}
	}
	long long int getOverlappingCount(uBasicNGSChrom* chrom, uBasicNGSChrom* otherChrom, char* overlapType) {
		string overlapTypeString(overlapType);
		if (overlapTypeString == "OVERLAP_PARTIAL") {
			return chrom->getOverlappingCount(*otherChrom, OverlapType::OVERLAP_PARTIAL);
		}
		else if (overlapTypeString == "OVERLAP_COMPLETE") {
			return chrom->getOverlappingCount(*otherChrom, OverlapType::OVERLAP_COMPLETE);
		}
		else if (overlapTypeString == "OVERLAP_CENTER") {
			return chrom->getOverlappingCount(*otherChrom, OverlapType::OVERLAP_CENTER);
		}
		else {
			throw runtime_error("getOverlappingCount: Invalid overlapType(" + overlapTypeString + ")");
		}
	}
	uBasicNGSChrom* getOverlappingChromBasic(uBasicNGSChrom* chrom, uBasicNGS* region, char* overlapType) {
		string overlapTypeString(overlapType);
		if (overlapTypeString == "OVERLAP_PARTIAL") {
			return new uBasicNGSChrom(chrom->getOverlapping(*region, OverlapType::OVERLAP_PARTIAL));
		}
		else if (overlapTypeString == "OVERLAP_COMPLETE") {
			return new uBasicNGSChrom(chrom->getOverlapping(*region, OverlapType::OVERLAP_COMPLETE));
		}
		else if (overlapTypeString == "OVERLAP_CENTER") {
			return new uBasicNGSChrom(chrom->getOverlapping(*region, OverlapType::OVERLAP_CENTER));
		}
		else {
			throw runtime_error("getOverlapping: Invalid overlapType(" + overlapTypeString + ")");
		}
	}
	long long int getOverlappingCountBasic(uBasicNGSChrom* chrom, uBasicNGS* basic, char* overlapType) {
		string overlapTypeString(overlapType);
		if (overlapTypeString == "OVERLAP_PARTIAL") {
			return chrom->getOverlappingCount(*basic, OverlapType::OVERLAP_PARTIAL);
		}
		else if (overlapTypeString == "OVERLAP_COMPLETE") {
			return chrom->getOverlappingCount(*basic, OverlapType::OVERLAP_COMPLETE);
		}
		else if (overlapTypeString == "OVERLAP_CENTER") {
			return chrom->getOverlappingCount(*basic, OverlapType::OVERLAP_CENTER);
		}
		else {
			throw runtime_error("getOverlappingCount: Invalid overlapType(" + overlapTypeString + ")");
		}
	}
	uBasicNGSChrom* getOverlappingChromRegion(uBasicNGSChrom* chrom, long int start, long int end, char* overlapType) {
		string overlapTypeString(overlapType);
		if (overlapTypeString == "OVERLAP_PARTIAL") {
			return new uBasicNGSChrom(chrom->getOverlapping(start, end, OverlapType::OVERLAP_PARTIAL));
		}
		else if (overlapTypeString == "OVERLAP_COMPLETE") {
			return new uBasicNGSChrom(chrom->getOverlapping(start, end, OverlapType::OVERLAP_COMPLETE));
		}
		else if (overlapTypeString == "OVERLAP_CENTER") {
			return new uBasicNGSChrom(chrom->getOverlapping(start, end, OverlapType::OVERLAP_CENTER));
		}
		else {
			throw runtime_error("getOverlapping: Invalid overlapType(" + overlapTypeString + ")");
		}
	}
	long long int getOverlappingCountRegion(uBasicNGSChrom* chrom, long int start, long int end, char* overlapType) {
		string overlapTypeString(overlapType);
		if (overlapTypeString == "OVERLAP_PARTIAL") {
			return chrom->getOverlappingCount(start, end, OverlapType::OVERLAP_PARTIAL);
		}
		else if (overlapTypeString == "OVERLAP_COMPLETE") {
			return chrom->getOverlappingCount(start, end, OverlapType::OVERLAP_COMPLETE);
		}
		else if (overlapTypeString == "OVERLAP_CENTER") {
			return chrom->getOverlappingCount(start, end, OverlapType::OVERLAP_CENTER);
		}
		else {
			throw runtime_error("getOverlappingCount: Invalid overlapType(" + overlapTypeString + ")");
		}
	}
	uBasicNGSChrom* getNotOverlapping(uBasicNGSChrom* chrom, uBasicNGSChrom* otherChrom, char* overlapType) {
		string overlapTypeString(overlapType);
		if (overlapTypeString == "OVERLAP_PARTIAL") {
			return new uBasicNGSChrom(chrom->getNotOverlapping(*otherChrom, OverlapType::OVERLAP_PARTIAL));
		}
		else if (overlapTypeString == "OVERLAP_COMPLETE") {
			return new uBasicNGSChrom(chrom->getNotOverlapping(*otherChrom, OverlapType::OVERLAP_COMPLETE));
		}
		else if (overlapTypeString == "OVERLAP_CENTER") {
			return new uBasicNGSChrom(chrom->getNotOverlapping(*otherChrom, OverlapType::OVERLAP_CENTER));
		}
		else {
			throw runtime_error("getNotOverlappingCount: Invalid overlapType(" + overlapTypeString + ")");
		}
	}

  /**< Wrap sortSites */
    void sortSites_basicChrom(uBasicNGSChrom* pChrom)
    {
        pChrom->sortSites();
    }

	 /**< Wrap getSubset */
    uBasicNGSChrom* getSubset_basicChrom(uBasicNGSChrom* pChrom, int pStart, int pEnd)
    {
        uBasicNGSChrom* returnChrom = new uBasicNGSChrom();
        *returnChrom= ( pChrom->getSubset(pStart,pEnd) );
        return returnChrom;
    }
    /**< getSubsetCOunt */
    long int getSubsetCount_basicChrom(uBasicNGSChrom* pChrom, int pStart, int pEnd)
    {
        return (pChrom->getSubsetCount(pStart,pEnd));
    }

    /**< Wraps removeSubsetre */
    uBasicNGSChrom* removeSubset_basicChrom(uBasicNGSChrom* pChrom,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSChrom* returnChrom = new uBasicNGSChrom();
        *returnChrom= ( pChrom->removeSubset(pStart,pEnd) );
        return returnChrom;
    }
     /**< Wraps getDistinct(string, start, end */
    uBasicNGSChrom* getDistinct_basicChrom(uBasicNGSChrom* pChrom,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSChrom* returnChrom = new uBasicNGSChrom();
        *returnChrom= pChrom->getDistinct(pStart,pEnd);
        return returnChrom;
    }
    /**< Wraps removeDistinct(string, start, end */
    uBasicNGSChrom* removeDistinct_basicChrom(uBasicNGSChrom* pChrom,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSChrom* returnChrom = new uBasicNGSChrom();
        *returnChrom= pChrom->removeDistinct(pStart,pEnd);
        return returnChrom;
    }



} // End of extern "C"
