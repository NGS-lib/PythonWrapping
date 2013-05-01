#include <iostream>
#include <string>
using namespace std;

class Foo{
public:
	Foo(string toPrint) : m_toPrint(toPrint) {}
	void bar(){
	    std::cout << m_toPrint << std::endl;
	}
private:
	string m_toPrint;
};

extern "C" {
    Foo* Foo_new(char* toPrint){ return new Foo(toPrint); }
    void Foo_bar(Foo* foo){ foo->bar(); }
}

