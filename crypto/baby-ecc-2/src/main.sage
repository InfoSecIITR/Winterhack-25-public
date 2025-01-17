from sage.all import *
from Crypto.Util.number import *
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from random import randint 
import hashlib 

import os
secret = os.urandom(64)

p = getPrime(24)
r = randint(2, 2 ** 16)

while True:
    a = randint(2, 2 ** 16)
    b = randint(2, 2 ** 16) 

    E = EllipticCurve(GF(p), [a, b])
    if not E.is_singular():
        print(p, a, b)
        break 
    
G = E.gens()[0]
P = r * G 

print(f"{G = }")
print(f"{P = }")

key = hashlib.sha256(str(r).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)
encrypted_secret = cipher.encrypt(pad(secret, AES.block_size))
print(f"{encrypted_secret = }")

assert secret == unpad(cipher.decrypt(encrypted_secret), AES.block_size)

secret_ = bytes.fromhex(str(input("Enter the secret (in hex): ")))
if secret == secret_:
    os.system("/bin/sh")