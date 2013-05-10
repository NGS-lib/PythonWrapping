GXX=g++
NGS_PATH=/home/cjbparlant/git-clones/class
NGS_INGLUDE=-Wl,--whole-archive $(NGS_PATH)/libs/libNGS.a -Wl,--no-whole-archive
CFLAGS=-O3 -Wall -std=c++11 -c -fPIC
LFLAGS=-shared -Wl,-soname,libfoo.so -lz
INCLUDE=-I$(NGS_PATH) -I$(NGS_PATH)/NGS

OBJECTS=foo.o
OBJECTS+=uBasicNGS.o
OBJECTS+=uBasicNGSChrom.o

.PHONY: all
all: libfoo.so

.PHONY: clean
clean:
	rm -f foo.o libfoo.so

.PHONY: exec
exec: libfoo.so
	./fooWrapper.py

libfoo.so: $(OBJECTS)
	$(GXX) $(LFLAGS) -o libfoo.so $^ $(NGS_INGLUDE)

%.o: %.cpp
	$(GXX) $(CFLAGS) $(INCLUDE) $< -o $@
