from Crypto.Util.number import isPrime
from pwn import *

io = process(["python3", "chall.py"])

io.recvuntil(b"N=")
N = int(io.recvline().strip())
io.recvuntil(b"e=")
e = int(io.recvline().strip())
io.recvuntil(b"ct=")
ct = int(io.recvline().strip())

l = 0
r = N

while l < r:
    m = (l + r) // 2
    prod = m * int(str(m), 16)

    if prod == N:
        if isPrime(m):
            print(m)
            break

    elif prod < N:
        l = m + 1

    else:
        r = m

p = m
q = N // p

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(ct, d, N)


io.sendlineafter(b": ", hex(m)[2:].encode())

io.interactive()
