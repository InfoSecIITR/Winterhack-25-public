from sage.all import *
from sage.groups.generic import bsgs
from Crypto.Util.number import *
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from random import randint 
from pwn import *
import hashlib 

# r = process(["python3", "main.sage"])
# r = remote("localhost", 6005)
r = remote("34.47.134.251", 6005)

Gx, Gy, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))
Px, Py, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))
p = int(r.recvline().strip().decode().split(" = ")[1])

a = ((Gy ** 2 - Py ** 2) - (Gx ** 3 - Px ** 3)) * (pow(Gx - Px, -1, p)) % p 
b = (Gy ** 2 - Gx ** 3 - a * Gx) % p

E = EllipticCurve(GF(p), [a, b])

G = E((Gx, Gy))
P = E((Px, Py))

def dlp_solve(G,A):
    primes = []
    point_order = G.order()
    for i in point_order.factor():
        if (len(primes) < 8):
            primes.append(i)
        else:
            break
    corresponding_dlp = [0] * len(primes)
    for i,(p_i, e_i) in enumerate(primes):
        for j in range(e_i):
            corresponding_dlp[i] += bsgs(G*(point_order//p_i),(A-(G*corresponding_dlp[i]))*(point_order//(p_i**(j+1))),(0,p_i),operation='+')*(p_i**j)
    return crt(corresponding_dlp,[p_i**e_i for (p_i,e_i) in primes])

secret = dlp_solve(G, P)

key = hashlib.sha256(str(secret).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)

encrypted_flag = eval(r.recvline().strip().decode().split(" = ")[1])
flag = unpad(cipher.decrypt(encrypted_flag), AES.block_size)
r.sendline(str(hex(bytes_to_long(flag))[2:]).encode())

r.interactive()