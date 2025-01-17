from Crypto.Cipher import AES
import os


def level1():
    print("Welcome to the first level!")

    key = os.urandom(16)
    nonce = os.urandom(12)
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    secret = os.urandom(32).hex().encode()

    print("Here's your encrypted secret:", cipher.encrypt(secret).hex())

    msg = input("Enter a message to be encrypted: ").strip()
    msg = bytes.fromhex(msg)
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    enc = cipher.encrypt(msg)
    print("Here is your encrypted message:", enc.hex())

    usr_msg = input("Please enter the secret code: ").strip()
    usr_msg = bytes.fromhex(usr_msg)
    if usr_msg == secret:
        print("Congratulations! You have passed this level.")
    else:
        print("Sorry! You have entered the wrong code.")
        exit(1)


def level2():
    print("Welcome to the second level!")
    key = os.urandom(16)
    nonce = os.urandom(12)

    print("Here are some encrypted secrets: ")
    for _ in range(42):
        secret = os.urandom(32).hex().encode()
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        print(cipher.encrypt(secret).hex())

    final_secret = os.urandom(32).hex()
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    print(cipher.encrypt(final_secret.encode()).hex())

    usr_msg = input("Please enter the secret code: ").strip()
    if usr_msg == final_secret:
        print("Congratulations! You have passed this level.")
    else:
        print("Sorry! You have entered the wrong code.")
        exit(1)


def main():
    print("Welcome to the challenge!")
    print("You have to pass 2 levels to get the flag.")

    try:
        level1()
        level2()
    except:
        print("Sorry! You failed.")
        exit(1)

    os.system("cat flag.txt")


if __name__ == "__main__":
    main()
