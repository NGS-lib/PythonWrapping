GXX=g++
NGS_PATH=/usr/include
NGS_INGLUDE=/usr/lib/libNGS.a -Wl,--no-whole-archive
CFLAGS=-O3 -Wall -std=c++11 -c -fPIC
LFLAGS=-shared -Wl,-soname,$(TARGET) -lz
INCLUDE=-I$(NGS_PATH) -I$(NGS_PATH)/NGS

OBJECTS+=uBasicNGS_wrapper.o
OBJECTS+=uBasicNGSChrom_wrapper.o
OBJECTS+=uBasicNGSExperiment_wrapper.o
OBJECTS+=uParser_Wrapper.o
OBJECTS+=uToken_Wrapper.o
OBJECTS+=uWriter_Wrapper.o
TARGET=libNGS_pyWrapper.so

.PHONY: all
all: $(TARGET)

.PHONY: exec
exec: $(TARGET)
	./uBasicNGS_wrapper.py
	./uBasicNGSChrom_wrapper.py
	./uBasicNGSExperiment_wrapper.py
	./uParser_wrapper.py
	./uWriter_wrapper.py
	./uToken_wrapper.py

.PHONY: basic
basic: $(TARGET)
	./uBasicNGS_wrapper.py

.PHONY: chrom
chrom: $(TARGET)
	./uBasicNGSChrom_wrapper.py

.PHONY: experiment
experiment: $(TARGET)
	./uBasicNGSExperiment_wrapper.py

.PHONY: parser
parser: $(TARGET)
	./uParser_wrapper.py

.PHONY: writer
writer: $(TARGET)
	./uWriter_wrapper.py

.PHONY: token
token: $(TARGET)
	./uToken_wrapper.py

.PHONY: clean
clean:
	rm -f $(TARGET)

$(TARGET): $(OBJECTS)
	$(GXX) $(LFLAGS) -o $(TARGET) $^ $(NGS_INGLUDE)

%.o: %.cpp
	$(GXX) $(CFLAGS) $(INCLUDE) $< -o $@
