from Crypto.Util.number import getPrime, isPrime, long_to_bytes, bytes_to_long
from gaussint import GaussianInteger as ZI
from secrets import randbits
from Crypto.Random import random
from subprocess import run

def get_gaussian_prime(nbits):
    while True:
        candidate_real = randbits(nbits-1) + (1 << nbits)
        candidate_imag = randbits(nbits-1) + (1 << nbits)
        if isPrime(candidate_real*candidate_real + candidate_imag*candidate_imag):
            candidate = ZI(candidate_real, candidate_imag)
            return candidate


def encrypt(z, pkey):
    n, e = pkey
    return pow(z, e, n)


def level0():
    print("==============LEVEL 0==============")
    print("Let's start with some basics.")

    e = getPrime(10)
    p = get_gaussian_prime(10)
    q = get_gaussian_prime(10)
    N = p * q

    x = random.randint(0, abs(N.r))
    y = random.randint(0, abs(N.i))
    P = ZI(x, y)
    Q = encrypt(P, (N, e))

    print(f"{N=}")
    print(f"{e=}")
    print(f"{P=}")
    print(f"Q = P ^ e mod N")

    print("What is Q? Answer in the format 'real(Q) imag(Q)'")
    ans = input('> ').strip().split()
    ans = ZI(int(ans[0]), int(ans[1]))

    assert Q == ans, "Wrong answer!"

    print("Good job! You passed level 0.")
    print("===================================")

def level1():
    print("==============LEVEL 1==============")

    e = getPrime(16)
    N = get_gaussian_prime(128)

    pkey = (N, e)

    x = random.randint(0, abs(N.r))
    y = random.randint(0, abs(N.i))
    P = ZI(x, y)
    Q = encrypt(P, pkey)

    print(f"{N=}")
    print(f"{e=}")
    print(f"{Q=} = P ^ e mod N")

    print("What is P? (answer in the format 'real(P) imag(P)')")
    ans = input('> ').strip().split()
    ans = ZI(int(ans[0]), int(ans[1]))
    assert P == ans, "Wrong answer!"
    print("Good job! You passed level 1.")
    print("===================================")

def level2():
    print("==============LEVEL 2==============")

    p = get_gaussian_prime(16)
    q = get_gaussian_prime(16)
    (N, e) = pkey = (p * q, 65537)

    x = random.randint(0, abs(N.r))
    y = random.randint(0, abs(N.i))
    P = ZI(x, y)
    Q = encrypt(P, pkey)

    print(f"{N=}")
    print(f"{e=}")
    print(f"{Q=} = P ^ e mod N")

    print("What is P? (answer in the format 'real(P) imag(P)')")
    ans = input('> ').strip().split()
    ans = ZI(int(ans[0]), int(ans[1]))
    assert P == ans, "Wrong answer!"
    print("Good job! You passed level 2.")
    print("===================================")

def level3():
    print("==============LEVEL 3==============")

    e = getPrime(16)
    p = get_gaussian_prime(64)
    q = get_gaussian_prime(64)
    N = p * q

    print(f'p^2 + q^2 = {p * p + q * q}')

    pkey = (N, e)

    x = random.randint(0, abs(N.r))
    y = random.randint(0, abs(N.i))
    P = ZI(x, y)
    Q = encrypt(P, pkey)

    print(f"{N=}")
    print(f"{e=}")
    print(f"{Q=} = P ^ e mod N")

    print("What is P? (answer in the format 'real(P) imag(P)')")
    ans = input('> ').strip().split()
    ans = ZI(int(ans[0]), int(ans[1]))
    assert P == ans, "Wrong answer!"
    print("Good job! You passed level 3.")
    print("===================================")

def level4():
    print("==============LEVEL 4==============")

    e = 0x10001
    p = get_gaussian_prime(81)
    q = get_gaussian_prime(81)
    N = p * q

    pkey = (N, e)

    flag = b'winterhack{RSA_0v3r_Z[I]_r1n6!_958f1cde196f65ca}'
    # print('[DEBUG] flag:', flag)

    assert len(flag) % 2 == 0, "Flag length must be even!"

    x = bytearray([flag[i] for i in range(0, len(flag), 2)])
    y = bytearray([flag[i] for i in range(1, len(flag), 2)])

    x = bytes_to_long(x)
    y = bytes_to_long(y)

    assert x * x + y * y < N.r * N.r + N.i * N.i, "Flag is too long!"

    P = ZI(x, y)
    Q = encrypt(P, pkey)

    es = [getPrime(15) for _ in range(3)]

    A = pow(ZI(13, 37), es[0], N)
    B = pow(ZI(69, 420), es[1], N)
    C = pow(ZI(1337, 80085), es[2], N)

    print(f'{A=} = {ZI(13, 37)} ^ {es[0]} mod N')
    print(f'{B=} = {ZI(69, 420)} ^ {es[1]} mod N')
    print(f'{C=} = {ZI(1337, 80085)} ^ {es[2]} mod N')
    print(f"{e=}")
    print(f"{Q=} = P ^ e mod N")

    # print(f'[DEBUG] {p=}')
    # print(f'[DEBUG] {q=}')
    
    print("What is P? (answer in the format 'real(P) imag(P)')")
    ans = input('> ').strip().split()
    ans = ZI(int(ans[0]), int(ans[1]))
    assert P == ans, "Wrong answer!"
    print("Good job! You passed level 4.")
    print("===================================")


if __name__ == "__main__":
    try:
        level0()
        level1()
        level2()
        level3()
        level4()
        print('Congratulations! You have passed all levels! :)')
    except Exception as e:
        print(e)
        print('You failed.')

    
