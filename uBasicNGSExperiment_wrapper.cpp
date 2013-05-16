#include <iostream>
#include <string>
#include <vector>
#include "NGS/uBasicNGS.h"

using namespace NGS;
using namespace std;


//    void replaceChr(const _CHROM_ &);
//    void removeChr(const std::string &);

//     _CHROM_ getChrom(const std::string & chrom) const;
//     const _CHROM_* getpChrom(const std::string & chrom) const;
//    _CHROM_* getpChrom(const std::string & chrom);
//    _BASE_ getSite(const std::string & pChr, long int pPosition)const;
//    _BASE_ getSite(typename std::vector<_BASE_>::const_iterator posItr)const;
//
//    _SELF_ getOverlapping(_SELF_ &compareExp, OverlapType type=OverlapType::OVERLAP_PARTIAL);
//    _SELF_ getOverlapping(_CHROM_ &compareChrom, OverlapType type=OverlapType::OVERLAP_PARTIAL);
//    _SELF_ getOverlapping(std::string chr, int start, int end, OverlapType type=OverlapType::OVERLAP_PARTIAL);
//
//    // TODO: getSubset overload that check every chromosome
//
//    // TODO: getDistinct overload that check every chromosome
//    // TODO: getDistinct overload with range vector
//    _SELF_ getDistinct(const std::string & pChr, const double pStart, const double pEnd, OverlapType type=OverlapType::OVERLAP_PARTIAL);
//    _SELF_ removeDistinct(const std::string & pChr,const double pStart, const double pEnd, OverlapType options=OverlapType::OVERLAP_PARTIAL);
//
//
//    long int getSubsetCount(const std::string & pChr, const double pStart, const double pEnd, const OverlapType overlap=OverlapType::OVERLAP_PARTIAL);
//    long int getSubsetCount(const _BASE_ & subsetReg, const OverlapType overlap=OverlapType::OVERLAP_PARTIAL);
//
//
//    int getChrCount(){return ExpMap.size();};
//
//    void setChrSize(std::string chr, int chrSize);
//    int getChrSize(std::string chr);
//    void divideItemsIntoBinofSize(int N, SplitType type=SplitType::STRICT);
//    void divideItemsIntoNBins(int N, SplitType type=SplitType::STRICT);





extern "C" {
	/** Constructors / Destructor */
	uBasicNGSExperiment* new_basicExperiment() {
		return new uBasicNGSExperiment();
	}

    /**< Overloads destructor */
	void delete_basicExperiment(uBasicNGSExperiment* pExp) {
		delete pExp;
		pExp = NULL;
	}

    /**< Wraps addData(uBasicNGS) */
    void addDataUnit_basicExperiment(uBasicNGSExperiment* pExp, uBasicNGS* pData){
            (pExp->addData(*pData));
    }
    /**< Wraps addData(uBasicChrom) */
    void addDataChrom_basicExperiment(uBasicNGSExperiment* pExp, uBasicNGSChrom* pData){
            (pExp->addData(*pData));
    }

    /**< Wraps isChrom() */
    bool isChrom_basicExperiment(uBasicNGSExperiment* pExp ,char* pChrom)
    {
        return (pExp->isChrom(pChrom));
    }
    /**< Wraps count() */
    long long count_basicExperiment(uBasicNGSExperiment* pExperiment){
        return (pExperiment->count());
    }
    /**< Wraps sortSites */
    void sortSites_basicExperiment(uBasicNGSExperiment* pExperiment)
    {
        pExperiment->sortSites();
    }
    /**< Wrapper of isSorted() */
    bool isSorted_basicExperiment(uBasicNGSExperiment* pExperiment){
      return(pExperiment->isSorted());
    }
    /**< Wrapper of loadWithParser(path, type) */
    /**< Note that passing a path of "" will default to stdout */
    void loadPathWithParser_basicExperiment(uBasicNGSExperiment* pExperiment,char* pPath, char* pType,long long pCount){
        if (pCount==0)
            pExperiment->loadWithParser(pPath,pType);
        else
            pExperiment->loadWithParser(pPath,pType,pCount);
    }
    void loadWithParser_basicExperiment(uBasicNGSExperiment* pExperiment,uParser * pParser, long long pCount){
        if (pCount==0)
            pExperiment->loadWithParser(*pParser);
        else
            pExperiment->loadWithParser(*pParser,pCount);
    }
    /**< Wrapper of inferChrSize() */
    void inferChrSize_basicExperiment(uBasicNGSExperiment* pExperiment)
    {
        pExperiment->inferChrSize();
    }
    /**< Wraps writeWithWriter(uWriter) */
    void writeWithWriter_basicExperiment(uBasicNGSExperiment* pExperiment,uWriter* pWriter){

        pExperiment->writeWithWriter(*pWriter);
    }
    /**< Wraps getSite(pos) */
    uBasicNGS* getSite_basicExperiment(uBasicNGSExperiment* pExperiment, char * pChr, int pPos){
        uBasicNGS * returnBasic = new uBasicNGS();

        *returnBasic = (pExperiment->getSite(pChr, pPos));
        return returnBasic;

    }
    /**< Wraps removesite(iterator) but takes a (int pos ) instead*/
    void removeSite_basicExperiment(uBasicNGSExperiment* pExperiment,char* pChr, int pos){
        pExperiment->removeSite(pExperiment->getpChrom(pChr)->begin()+pos);
    }

    /**< Wraps removeChr */
    void removeChr_basicExperiment(uBasicNGSExperiment* pExperiment, char * pChr)
    {
        pExperiment->removeChr(pChr);
    }
    /**< Wraps findPreceding */
    int findPrecedingSitePos_basicExperiment(uBasicNGSExperiment* pExperiment, char * pChr, int value)
    {
        auto itr = pExperiment->findPrecedingSite(pChr,value);
        int pos = (itr-pExperiment->getpChrom(pChr)->begin());
        return pos;
    }
    /**< Wraps findNextSite */
    int findNextSitePos_basicExperiment(uBasicNGSExperiment* pExperiment, char * pChr, int value)
    {
        auto itr = pExperiment->findNextSite(pChr,value);
        int pos = (itr-pExperiment->getpChrom(pChr)->begin());
        return pos;
    }

    /**< Wrap getSubset */
    uBasicNGSChrom* getSubset_basicExperiment(uBasicNGSExperiment* pExperiment,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSChrom* returnChrom = new uBasicNGSChrom();
        *returnChrom= ( pExperiment->getSubset(pChr,pStart,pEnd) );
        return returnChrom;
    }
    /**< Wraps removeSubsetre */
    uBasicNGSChrom* removeSubset_basicExperiment(uBasicNGSExperiment* pExperiment,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSChrom* returnChrom = new uBasicNGSChrom();
        *returnChrom= ( pExperiment->removeSubset(pChr,pStart,pEnd) );
        return returnChrom;
    }



}
