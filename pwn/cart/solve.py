#!/usr/bin/env python3

from pwn import *

exe = ELF("./cart_titan")
# libc = ELF("./libc.so.6")
# ld = ELF("./ld-linux.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("34.47.134.251", 5007)

    return r


def main():
    r = conn()
    r.sendline(b'')
    r.sendline(b'PWNIng_Is_The_Best_Category')
    
    

    r.interactive()


if __name__ == "__main__":
    main()
