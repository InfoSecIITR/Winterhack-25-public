# solve.py
from pwn import *
from functools import reduce
from math import gcd
from Crypto.Util.number import long_to_bytes, isPrime

context.log_level = 'critical'

def solve():
    p = process(['python3', 'chall.py'])

    n = int(p.recvline().strip().split()[-1])

    s = []
    for _ in range(6):
        s.append(int(p.recvline().strip(), 16))

    p.close()

    def crack_unknown_multiplier(states, modulus):
        multiplier = (states[2] - states[1]) * pow(states[1] - states[0], -1, modulus) % modulus
        return multiplier

    def crack_unknown_modulus(states):
        diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
        zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
        modulus = abs(reduce(gcd, zeroes))
        return modulus

    p = crack_unknown_modulus(s)
    a_pow_n = crack_unknown_multiplier(s, p)
    if gcd(n, p - 1) != 1:
        raise Exception(f'Cannot solve for {n=}')
    
    phi = p - 1
    d = pow(n, -1, phi)
    a = pow(a_pow_n, d, p)

    series_sum = sum(pow(a,i,p) for i in range(n))

    if gcd(series_sum, p) != 1:
        raise Exception(f'Cannot solve for {series_sum=}')

    c = ((s[1] - s[0] * a_pow_n) * pow(series_sum, -1, p)) % p

    es = [x for x in range(2**10, 2**11+1) if isPrime(x)]
    m = set()
    for e in es:

        x = (s[0] - c) * pow(a, -1, p) % p
        d = pow(e, -1, phi)
        m_ = pow(x, d, p)
        m_ = long_to_bytes(m_)
        m.add(m_)

        e += 1

    return m

if __name__ == '__main__':
    while True:
        try:
            ms = solve()
            for m in ms:
                if b'winter' in m:
                    print(m.decode())
                    exit(0)
        except Exception as e:
            if e is KeyboardInterrupt:
                break
            else:
                print(e)
            continue
