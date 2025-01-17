from sage.all import *
from pwn import * 

# r = process(["python3", "main.sage"])
# r = remote("localhost", 6002)
r = remote("34.47.134.251", 6002)
p, a, b = map(int, r.recvline().strip().decode().split(" "))

E = EllipticCurve(GF(p), [a, b])
Gx, Gy, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))
Px, Py, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))

G = E((Gx, Gy))
P = E((Px, Py))

for i in range(2, 2 ** 10):
    if i * G == P:
        r.sendline(str(i).encode())
        r.interactive()
        exit(0)