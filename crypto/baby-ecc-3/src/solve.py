from sage.all import *
from Crypto.Util.number import *
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from random import randint 
from pwn import *
import hashlib 

# r = process(["python3", "main.sage"])
# r = remote("localhost", 6004)
r = remote("34.47.134.251", 6004)
p = int(r.recvline().strip().decode())

Gx, Gy, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))
Px, Py, _ = map(int, r.recvline().strip().decode().split(" = ")[1][1:-1].split(" : "))

a = ((Gy ** 2 - Py ** 2) - (Gx ** 3 - Px ** 3)) * (pow(Gx - Px, -1, p)) % p 
b = (Gy ** 2 - Gx ** 3 - a * Gx) % p

key = hashlib.sha256(str(pow(a, b, p)).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)

encrypted_flag = eval(r.recvline().strip().decode().split(" = ")[1])
flag = unpad(cipher.decrypt(encrypted_flag), AES.block_size)
r.sendline(str(hex(bytes_to_long(flag))[2:]).encode())

r.interactive()