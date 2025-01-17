from sage.all import * 
from Crypto.Util.number import *
from secrets import p, a, b
from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
import hashlib 

import os
secret = os.urandom(64)

E = EllipticCurve(GF(p), [a, b])
G = E.gens()[0]

r = randint(1, 2 ** 90)
P = r * G 

print(f"{G = }")
print(f"{P = }")
print(f"{p = }")

key = hashlib.sha256(str(r).encode()).digest()
cipher = AES.new(key, AES.MODE_ECB)
encrypted_secret = cipher.encrypt(pad(secret, AES.block_size))
print(f"{encrypted_secret = }")

assert secret == unpad(cipher.decrypt(encrypted_secret), AES.block_size)

secret_ = bytes.fromhex(str(input("Enter the secret (in hex): ")))
if secret == secret_:
    os.system("/bin/sh")