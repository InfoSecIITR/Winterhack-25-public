#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os


def level1():
    print("Welcome to the first level!")
    key = os.urandom(16)
    cipher = AES.new(key, AES.MODE_ECB)
    secret = os.urandom(32).hex().encode()

    print("Here's your encrypted secret:", cipher.encrypt(secret).hex())

    enc = input("Enter a message to be decrypted: ").strip()
    dec = cipher.decrypt(bytes.fromhex(enc))

    if dec == secret:
        print("You cannot decrypt the encrypted secret.")
        exit(1)
    else:
        print("Here is your decrypted message:", dec.hex())

    usr_msg = input("Please enter the secret code: ").strip()
    usr_msg = bytes.fromhex(usr_msg)
    if usr_msg == secret:
        print("Congratulations! You have passed this level.")
    else:
        print("Sorry! The code is incorrect.")
        print("Goodbye!")
        exit(1)


def level2():
    print("Welcome to the second level!")
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    msg = 'winner=false'.encode()
    msg = pad(msg, 16)
    enc = iv.hex() + cipher.encrypt(msg).hex()
    print("Here's your encrypted message:", enc)

    usr_msg = input("Enter a message to be decrypted: ").strip()
    iv = bytes.fromhex(usr_msg[:32])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    dec = cipher.decrypt(bytes.fromhex(usr_msg[32:]))

    if b'winner=true' in dec:
        print("Congratulations! You have passed this level.")
        return
    else:
        print("Sorry! You didn't win.")
        exit(1)


def main():
    print("Welcome to the challenge!")
    print("You have to pass 2 levels to get the flag.")

    try:
        level1()
        level2()
    except:
        print("Something went wrong!")
        exit(1)

    os.system("cat flag.txt")


if __name__ == "__main__":
    main()
