# chall.py
from Crypto.Util.number import getPrime, bytes_to_long
from Crypto.Random.random import randint
from subprocess import run

class LKG:
    def __init__(self, seed):
        self.p = getPrime(1024)
        self.c = getPrime(1024)
        self.a = getPrime(1024)

        self.state = pow(seed, getPrime(11), self.p)

    def __next__(self):
        self.state = (self.state * self.a + self.c) % self.p
        return self.state

flag = b'winterhack{c0n6r47ul4710n5!_y0u\'r3_4_c3r71f13d_LKG_cr4ck3r_n0w_ab3dc378120cd36f}'
seed = bytes_to_long(flag)
rng = LKG(seed)
n = randint(1000, 1500)
print(f"{n = }")
for _ in range(6):
    print(hex(next(rng))[2:])
    for _ in range(n-1):
        next(rng)