from Crypto.Util.number import *
import os

e = 0x10001
nbits = 512


def gen_params(bit_length=256):
    found = False
    while not found:
        p = getPrime(bit_length)
        q = int(str(p), 16)
        found = isPrime(q)

    return p*q


N = gen_params(nbits)
m = os.urandom(32)
m = bytes_to_long(m)
ct = pow(m, e, N)


print(f"{N=}")
print(f"{e=}")
print(f"{ct=}")


m_ = input("Enter the original message(hex): ")
m_ = int(m_, 16)

if m_ == m:
    os.system("cat flag.txt")
else:
    print("Try again! ")
