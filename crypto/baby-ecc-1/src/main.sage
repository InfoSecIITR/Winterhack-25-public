from sage.all import *
from Crypto.Util.number import *
from random import randint 
from flag import flag 
import os

p = getPrime(16)
r = randint(2, 2 ** 10)

while True:
    a = randint(2, 2 ** 10)
    b = randint(2, 2 ** 10) 

    E = EllipticCurve(GF(p), [a, b])
    if not E.is_singular():
        print(p, a, b)
        break 
    
G = E.gens()[0]
P = r * G 

print(f"{G = }")
print(f"{P = }")

r_ = int(input("Please enter the value for r: "))
if r_ == r:
    os.system("/bin/sh")
else:
    print("Check this out: https://cryptohack.org/challenges/ecc/")