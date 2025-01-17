from Crypto.Util.number import *
from pwn import * 
from math import gcd 

def squareroot(x):
    l = 1 
    r = 10 ** 3000 
    while l < r:
        mid = (l + r) // 2 
        if mid ** 2 > x:
            r = mid - 1 
        elif mid ** 2 < x:
            l = mid + 1 
        else:
            l = mid 
            r = mid 
            break 

    if l == r:
        return l 
    else: 
        return -1

def cuberoot(x):
    l = 1 
    r = 10 ** 3000 
    while l < r:
        mid = (l + r) // 2 
        if mid ** 3 > x:
            r = mid - 1 
        elif mid ** 3 < x:
            l = mid + 1 
        else:
            l = mid 
            r = mid 
            break 

    if l == r:
        return l 
    else: 
        return -1
 
# r = process(["python3", "main.py"], level='debug')
# r = remote("localhost", 6001)
r = remote("34.47.134.251", 6001)

r.recvuntil(b"0/8\n")
c = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
p = int(r.recvline().strip().decode().split(" = ")[1])

m = cuberoot(c)
r.sendline(str(m).encode()) 

r.recvuntil(b"1/8\n")
c = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
p = int(r.recvline().strip().decode().split(" = ")[1])

d = pow(e, -1, p - 1) 
m = pow(c, d, p) 
r.sendline(str(m).encode())

r.recvuntil(b"2/8\n")
c = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
N = int(r.recvline().strip().decode().split(" = ")[1])

p = squareroot(N)
phi = p * (p - 1) 
d = pow(e, -1, phi) 
m = pow(c, d, N)
r.sendline(str(m).encode())

r.recvuntil(b"3/8\n")
c = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
N = int(r.recvline().strip().decode().split(" = ")[1])

save = N 

phi = 1
primes = {}
for i in range(2 ** 17):
    if isPrime(i):
        while save % i == 0:
            if i not in primes:
                primes[i] = 1
            else:
                primes[i] += 1 
            
            save //= i 
        
for i in primes:
    exp = primes[i]
    factor = i ** (exp - 1) * (i - 1) 
    phi *= factor 

d = pow(e, -1, phi) 
m = pow(c, d, N)
r.sendline(str(m).encode()) 

r.recvuntil(b"4/8\n")
N = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
c = int(r.recvline().strip().decode().split(" = ")[1])
e_ = int(r.recvline().strip().decode().split(" = ")[1])
c_ = int(r.recvline().strip().decode().split(" = ")[1])

x = pow(e, -1, e_)
y = (1 - x * e) // (e_)

m = (pow(c, x, N) * pow(c_, y, N)) % N
r.sendline(str(m).encode())

r.recvuntil(b"5/8\n")
e = int(r.recvline().strip().decode().split(" = ")[1])
N = int(r.recvline().strip().decode().split(" = ")[1])
c = int(r.recvline().strip().decode().split(" = ")[1])
N_ = int(r.recvline().strip().decode().split(" = ")[1])
c_ = int(r.recvline().strip().decode().split(" = ")[1])

p = gcd(N, N_)
q = N // p 
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi) 

m = pow(c, d, N)
r.sendline(str(m).encode())

r.recvuntil(b"6/8\n")
c = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
N = int(r.recvline().strip().decode().split(" = ")[1])
l = int(r.recvline().strip().decode().split(" = ")[1])
x = int(r.recvline().strip().decode().split(" = ")[1])
y = int(r.recvline().strip().decode().split(" = ")[1])

p = (l * pow(x, -1, y)) % y
q = N // p 
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi) 
m = pow(c, d, N) 

r.sendline(str(m).encode())

r.recvuntil(b"7/8\n")
c = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
N = int(r.recvline().strip().decode().split(" = ")[1])
s = int(r.recvline().strip().decode().split(" = ")[1])

phi = N - s + 1 
d = pow(e, -1, phi) 
m = pow(c, d, N) 
r.sendline(str(m).encode())

r.recvuntil(b"8/8\n")
c = int(r.recvline().strip().decode().split(" = ")[1])
e = int(r.recvline().strip().decode().split(" = ")[1])
N = int(r.recvline().strip().decode().split(" = ")[1])
s = int(r.recvline().strip().decode().split(" = ")[1])

phi = N - s + 1 
d = pow(e, -1, phi) 
m = pow(c, d, N) 
r.sendline(str(m).encode())

r.interactive() 