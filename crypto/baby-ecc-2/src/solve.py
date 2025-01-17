from sage.all import *
from Crypto.Util.number import *
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from random import randint 
from pwn import *
import hashlib 

# r = process(["python3", "main.sage"])
# r = remote("localhost", 6003)
r = remote("34.47.134.251", 6003)
p, a, b = map(int, r.recvline().strip().decode().split(" "))

E = EllipticCurve(GF(p), [a, b])
Gx, Gy, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))
Px, Py, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))

G = E((Gx, Gy))
P = E((Px, Py))

dlog = 1 
for i in range(2, 2 ** 16):
    if i * G == P:
        dlog = i 
        break 

key = hashlib.sha256(str(dlog).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)

encrypted_flag = eval(r.recvline().strip().decode().split(" = ")[1])
flag = unpad(cipher.decrypt(encrypted_flag), AES.block_size)
r.sendline(str(hex(bytes_to_long(flag))[2:]).encode())

r.interactive()