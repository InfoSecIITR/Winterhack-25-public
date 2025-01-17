from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
from random import randint


def level1():
    print("Welcome to the first level!")
    key = os.urandom(16)
    cipher = AES.new(key, AES.MODE_ECB)
    prefix = b"All the very best! I hope you solve this challenge."
    secret_msg = os.urandom(randint(16, 32))

    while True:
        cmd = input("[cmd] ").strip()
        if cmd == "exit":
            exit(1)

        elif cmd == "secret":
            enc = input("Enter the secret code: ").strip()
            enc = bytes.fromhex(enc)
            if enc == secret_msg:
                print("Congratulations! You have passed this level.")
                break
            else:
                print("Sorry! You have entered the wrong code.")
                exit(1)

        elif cmd == "encrypt":
            msg = input("Enter a message to be encrypted: ").strip()
            msg = bytes.fromhex(msg)
            to_enc = pad(prefix+msg+secret_msg, 16)
            enc = cipher.encrypt(to_enc)
            print("Here is your encrypted message:", enc.hex())

        else:
            print("Invalid command!")
            exit(1)


def level2():
    print("Welcome to the final level!")
    key = os.urandom(16)
    msg = b"Please give me the flag."

    while True:
        enc = input("Enter the encrypted secret code: ").strip()
        enc = bytes.fromhex(enc)
        iv = enc[:16]
        enc = enc[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        dec = cipher.decrypt(enc)
        padding_byte = dec[0]
        padding_len = ord(dec[:1])

        if padding_byte != 0 and all([x == padding_byte for x in dec[:padding_len]]):
            user_msg = dec[padding_len:]
            if user_msg == msg:
                print("Congratulations! You have passed the final level.")
                break
            else:
                print("Sorry! You have entered the wrong message.")
        else:
            print("Invalid padding!")


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
