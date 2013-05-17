#include <iostream>
#include <string>
#include <vector>
#include "NGS/uBasicNGS.h"

using namespace NGS;
using namespace std;






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

    /**< Wrapper ofr setChrSize */
    void setChrSize_basicExperiment(uBasicNGSExperiment* pExperiment, char* pChr, int chrSize)
    {
        pExperiment->setChrSize(pChr,chrSize);
    }
    /**< Wrapepr of getChrSize */
    int getChrSize_basicExperiment(uBasicNGSExperiment* pExperiment, char* pChr){
        return pExperiment->getChrSize(pChr);
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
    /**< Returns a position rather then an iterator */
    int findPrecedingSitePos_basicExperiment(uBasicNGSExperiment* pExperiment, char * pChr, int value)
    {
        auto itr = pExperiment->findPrecedingSite(pChr,value);
        int pos = (itr-pExperiment->getpChrom(pChr)->begin());
        return pos;
    }
    /**< Wraps findNextSite */
    /**< Returns a position rather then an iterator */
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
    /**< Wraps replaceChr(uBasicNGSChrom */
    void replaceChr_basicExperiment(uBasicNGSExperiment* pExperiment, uBasicNGSChrom* pChrom)
    {
        pExperiment->replaceChr(*pChrom);
    }

    /**< Wraps getOverlapping(uBasicNGSExperiment */
    uBasicNGSExperiment* getOverlapping_fromExp_basicExperiment(uBasicNGSExperiment* pExperiment,uBasicNGSExperiment* pCompExperiment)
    {
        uBasicNGSExperiment* returnExp = new uBasicNGSExperiment();
        *returnExp= pExperiment->getOverlapping(*pCompExperiment);
        return returnExp;
    }
     /**< Wraps getOverlapping(uBasicNGSChrom */
    uBasicNGSExperiment* getOverlapping_fromChrom_basicExperiment(uBasicNGSExperiment* pExperiment,uBasicNGSChrom* pCompChrom)
    {
        uBasicNGSExperiment* returnExp = new uBasicNGSExperiment();
        *returnExp= pExperiment->getOverlapping(*pCompChrom);
        return returnExp;
    }
    /**< Wraps getOverlapping(string, start, end */
    uBasicNGSExperiment* getOverlapping_fromRegion_basicExperiment(uBasicNGSExperiment* pExperiment,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSExperiment* returnExp = new uBasicNGSExperiment();
        *returnExp= pExperiment->getOverlapping(pChr,pStart,pEnd);
        return returnExp;
    }


    /**< Wraps getDistinct(string, start, end */
    uBasicNGSExperiment* getDistinct_basicExperiment(uBasicNGSExperiment* pExperiment,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSExperiment* returnExp = new uBasicNGSExperiment();
        *returnExp= pExperiment->getDistinct(pChr,pStart,pEnd);
        return returnExp;
    }
    /**< Wraps removeDistinct(string, start, end */
    uBasicNGSExperiment* removeDistinct_basicExperiment(uBasicNGSExperiment* pExperiment,char* pChr, int pStart, int pEnd)
    {
        uBasicNGSExperiment* returnExp = new uBasicNGSExperiment();
        *returnExp= pExperiment->removeDistinct(pChr,pStart,pEnd);
        return returnExp;
    }

    /**< Wrapper for get chrCount */
    int getChrCount_basicExperiment(uBasicNGSExperiment* pExperiment)
    {
        return pExperiment->getChrCount();

    }

    int getSubsetCount_region_basicExperiment(uBasicNGSExperiment* pExperiment, char* pChr, int start, int end)
    {
        return pExperiment->getSubsetCount(pChr,start,end);
    }

//     _CHROM_ getChrom(const std::string & chrom) const;
//     const _CHROM_* getpChrom(const std::string & chrom) const;
//    _CHROM_* getpChrom(const std::string & chrom);

//    void divideItemsIntoBinofSize(int N, SplitType type=SplitType::STRICT);
//    void divideItemsIntoNBins(int N, SplitType type=SplitType::STRICT);



}
