CXX		  := clang++
CXXFLAGS  := -std=c++20 -Wall -Wextra -O0
CXXFLAGS  += -fuse-ld=lld
CXXFLAGS  += -g0 -fstack-protector-strong
CXXFLAGS  += -lcrypto -lssl -static-libgcc -static-libstdc++

all: chall

chall: chall.cpp

.PHONY: clean
clean:
	rm -f chall
