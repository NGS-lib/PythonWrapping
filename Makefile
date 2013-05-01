GXX=g++
CFLAGS=-O3 -Wall -std=c++11 -c -fPIC -lz
LFLAGS=-shared -Wl,-soname,libfoo.so -l/home/cjbparlant/git-clones/class/libs
INCLUDE=-I/home/cjbparlant/git-clones/class -I/home/cjbparlant/git-clones/class/NGS
#LIB=/home/cjbparlant/git-clones/class/libs/libNGS.a
#LIB=Wl,--whole-archive /home/cjbparlant/git-clones/class/libs/libNGS.a -Wl,--no-whole-archive
LIB=Wl,--whole-archive -lNGS -Wl,--no-whole-archive
#LIB=Wl,--whole-archive ./libNGS.a -Wl,--no-whole-archive
ZLIB=-lz

.PHONY: all
all: libfoo.so

.PHONY: clean
clean:
	rm -f foo.o libfoo.so

libfoo.so: foo.o
	g++ -shared -Wl,-soname,libfoo.so -o libfoo.so foo.o -Wl,--whole-archive /home/cjbparlant/git-clones/class/libs/libNGS.a -Wl,--no-whole-archive
#	$(GXX) $(LFLAGS) $(ZLIB) -o libfoo.so foo.o $(LIB)   
#	g++ -shared -Wl,-soname,libfoo.so -o libfoo.so  foo.o
#	g++ -shared -Wl,-so_install_name -o libfoo.so  foo.o

foo.o: foo.cpp
	$(GXX) $(CFLAGS) $(INCLUDE) foo.cpp -o foo.o
#	g++ -c -fPIC foo.cpp -o foo.o
