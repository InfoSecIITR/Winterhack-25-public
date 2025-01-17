CC     := clang
CFLAGS := -O0 -Wall -std=c2x -g0
CFLAGS += -Wl,-z,relro
CFLAGS += -fno-stack-protector
CFLAGS += -fuse-ld=lld
CFLAGS += -fno-unroll-loops
CFLAGS += -pedantic

all: chall
	./chall

chall: chall.c

debug:
	$(MAKE) CFLAGS="$(CFLAGS) -g -DDEBUG" all

.PHONY: clean
clean:
	rm chall