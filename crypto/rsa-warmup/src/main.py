from Crypto.Util.number import *
from flag import flag 
from math import prod
import random 
import os 

introduction_message = """ 
---------------------------------------------------------
| Let's test your understanding of the RSA cryptosystem |
---------------------------------------------------------
"""

success_message = """
Good job! Time for the next level.
"""

fail_message = """
Better luck next time! 
"""

def level0():
    p = getPrime(128)
    
    e = 0x03 
    m = random.randint(2 ** 31, 2 ** 32)
    c = pow(m, e, p)

    print(f"{c = }")
    print(f"{e = }")
    print(f"{p = }")

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def level1():
    p = getPrime(128)
    
    e = 0x10001
    m = random.randint(2 ** 31, 2 ** 32)
    c = pow(m, e, p)

    print(f"{c = }")
    print(f"{e = }")
    print(f"{p = }")

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def level2():
    p, q = [getPrime(1024) for _ in range(2)]
    N = p * p 

    e = 0x10001 
    m = random.randint(2 ** 1023, 2 ** 1024)
    c = pow(m, e, N)

    print(f"{c = }")
    print(f"{e = }")
    print(f"{N = }")

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def level3():
    primes = [getPrime(16) for _ in range(128)]
    N = prod(primes) 
    e = 0x10001 

    m = random.randint(2 ** 511, 2 ** 512)
    c = pow(m, e, N) 

    print(f"{c = }")
    print(f"{e = }")
    print(f"{N = }")      

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False   

def level4():
    p, q = [getPrime(1024) for _ in range(2)]
    N = p * q 
    m = random.randint(2 ** 1023, 2 ** 1024) 

    e = 0x10001
    c = pow(m, e, N)

    e_ = 0x10001 - 0x10 
    c_ = pow(m, e_, N) 

    print(f"{N = }")
    print(f"{e = }")
    print(f"{c = }")
    print(f"{e_ = }")
    print(f"{c_ = }")

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def level5():
    p, q, r = [getPrime(1024) for _ in range(3)]
    m = random.randint(2 ** 1023, 2 ** 1024) 
    e = 0x10001

    N = p * q
    c = pow(m, e, N)

    N_ = p * r
    c_ = pow(m, e, N_) 

    print(f"{e = }")
    print(f"{N = }")
    print(f"{c = }")
    print(f"{N_ = }")
    print(f"{c_ = }")

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def level6():
    p, q = [getPrime(1024) for _ in range(2)]
    e = 0x10001 
    N = p * q
    m = random.randint(2 ** 1023, 2 ** 1024)

    x, y = [random.randint(2 ** 1023, 2 ** 1024) for _ in range(2)]
    l = x * p - y * q 

    c = pow(m, e, N)
    print(f"{c = }")
    print(f"{e = }")
    print(f"{N = }")
    print(f"{l = }")
    print(f"{x = }")
    print(f"{y = }")

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def level7():
    p, q = [getPrime(1024) for _ in range(2)]
    N = p * q 
    e = 0x10001
    m = random.randint(2 ** 1023, 2 ** 1024) 

    s = (pow(p, q, N) + pow(q, p, N)) % N 
    c = pow(m, e, N) 
    
    print(f"{c = }")
    print(f"{e = }")
    print(f"{N = }")
    print(f"{s = }") 

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def level8():
    p, q = [getPrime(1024) for _ in range(2)]
    phi = (p - 1) * (q - 1)
    N = p * q 
    e = 0x10001
    m = random.randint(2 ** 1023, 2 ** 1024) 

    a, b = [random.randint(2, 2 ** 256) for _ in range(2)]
    s = (pow(p, pow(q, a, phi), N) + pow(q, pow(p, b, phi), N)) % N 
    c = pow(m, e, N) 
    
    print(f"{c = }")
    print(f"{e = }")
    print(f"{N = }")
    print(f"{s = }") 

    m_ = int(input("What is the plaintext?\n"))
    if m_ == m:
        return True 

    return False 

def main():
    count = 0
    print(introduction_message) 

    while True:
        print(f"Current Level: {count}/8")
        
        if count == 0:
            if level0():
                count += 1 
                print(success_message)
            else:
                print(fail_message)
                exit(0)
        elif count == 1: 
            if level1():
                count += 1 
                print(success_message)
            else:
                print(fail_message)
                exit(0)
        elif count == 2:
            if level2():
                count += 1 
                print(success_message)
            else:
                print(fail_message)
                exit(0)
        elif count == 3:
            if level3():
                count += 1 
                print(success_message)
            else: 
                print(fail_message)
                exit(0) 
        elif count == 4:
            if level4():
                count += 1 
                print(success_message)
            else:
                print(fail_message)
                exit(0)
        elif count == 5:
            if level5():
                count += 1 
                print(success_message)
            else:
                print(fail_message)
                exit(0)
        elif count == 6:
            if level6():
                count += 1 
                print(success_message)
            else:
                print(fail_message)
                exit(0)
        elif count == 7:
            if level7():
                count += 1 
                print(success_message)
            else:
                print(fail_message)
                exit(0)
        elif count == 8:
            if level8():
                print("Well done!")
                os.system("/bin/sh")
            else:
                print(fail_message)
                exit(0)
main()