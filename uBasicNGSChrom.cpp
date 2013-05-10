#include "NGS++.h"

using namespace NGS;
using namespace std;

extern "C" {
	/** Constructors */
	uBasicNGSChrom* New_basicChrom() {
		return new uBasicNGSChrom();
	}
	uBasicNGSChrom* New_basicChromName(char* chrName) {
		return new uBasicNGSChrom(chrName);
	}
	uBasicNGSChrom* New_basicChromNameSize(char* chrName, long long int chrSize) {
		return new uBasicNGSChrom(chrName, chrSize);
	}
	/** Setters */
	void setChromSize(uBasicNGSChrom* chrom, long long int size) {
		chrom->setChromSize(size);
	}
} // End of extern "C"
