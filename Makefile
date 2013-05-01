.PHONY: all
all: libfoo.so

.PHONY: clean
clean:
	rm -f foo.o libfoo.so

libfoo.so: foo.o
	g++ -shared -Wl,-soname,libfoo.so -o libfoo.so  foo.o
#	g++ -shared -Wl,-so_install_name -o libfoo.so  foo.o

foo.o: foo.cpp
	g++ -c -fPIC foo.cpp -o foo.o
