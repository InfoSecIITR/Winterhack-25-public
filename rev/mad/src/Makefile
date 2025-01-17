CC     := clang
CFLAGS := -s -O1 -Wall -std=c2x -g0
CFLAGS += -Wl,-z,relro
CFLAGS += -fstack-protector
CFLAGS += -fuse-ld=lld
CFLAGS += -fno-unroll-loops

all: chall
	./chall

chall: chall.c

debug:
	$(MAKE) CFLAGS="$(CFLAGS) -g -DDEBUG" all

.PHONY: clean
clean:
	rm chall