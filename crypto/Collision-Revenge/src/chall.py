from hashlib import md5, sha1
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import random
import string
from secret import secret_codes
from subprocess import run

assert len(secret_codes) == 16
assert all(len(code) <= 16 for code in secret_codes)

secret_code = random.choice(secret_codes)

secret = ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(8)])
secret = secret.encode()
secret = bytes_to_long(secret)


history = []

tries = 3

print(f'Use this as your secret code: {secret_code.decode()}')

try:
    while tries > 0:
        print(f'Tries left: {tries}')

        m1 = bytes.fromhex(input('Provide the hex of first message: '))
        m2 = bytes.fromhex(input('Provide the hex of second message: '))

        if m1 == m2:
            print('Really huh?')
            tries -= 1
            continue

        if m1[:32] in history or m2[:32] in history:
            print('You have already provided similar messages before. You still lose a try.')
            tries -= 1
            continue

        if not m1.startswith(secret_code) and not m2.startswith(secret_code):
            print('At least one of the messages should start with the secret code!')
            tries -= 1
            continue

        h1 = md5(m1).digest()
        h2 = md5(m2).digest()

        if h1 != h2:
            print('The hashes do not match >:(')
            tries -= 1
            continue

        h1 = bin(bytes_to_long(sha1(m1).digest()))[2:34]
        h2 = bin(bytes_to_long(sha1(m2).digest()))[2:34]

        if h1 != h2:
            print('The hashes do not match >:(')
            tries -= 1
            continue

        print('Woah! Both messages have the same signature.')

        history.append(m1[:32])
        history.append(m2[:32])

        n = 16
        num = int(input(f'Give me a number with no more than {n} set bits and I will reveal those bits of the secret to you: '))
        if num.bit_count() > n:
            print(f'Read the rules properly. No more than {n} bits allowed.')
            tries -= 1
            continue

        print("Revealing bits: ", secret & num)
        tries -= 1
    
    guess = input('Guess the secret: ')
    secret = long_to_bytes(secret).decode()
    if guess == secret:
        flag = 'winterhack{600d_j0b_0n_5p3nd1n6_h0ur5_0f_c0mpu74710n!_y0u_r34lly_d353rv3_7h15_fl46_9f0812948fba2852d}'
        print(f'You guessed correctly! Here is your flag: {flag}')
    else:
        print('NGMI.')

except:
    print('Invalid input >:(')

