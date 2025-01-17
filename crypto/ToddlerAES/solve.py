from pwn import *

io = process(['python3', 'chall.py'], level='debug')

# Level 1
io.recvuntil(b"Here's your encrypted secret: ")
enc_secret = io.recvline().decode().strip()

io.sendlineafter(b"Enter a message to be encrypted: ", enc_secret.encode())
io.recvuntil(b"Here is your encrypted message: ")

secret = io.recvline().decode().strip()

io.sendlineafter(b"Please enter the secret code: ", secret.encode())


# Level 2
io.recvlines(3)
enc_secrets = []
num_secrets = 42

for _ in range(num_secrets+1):
    enc_secret = io.recvline().decode().strip()
    enc_secrets.append(bytes.fromhex(enc_secret))

final_secret = enc_secrets[-1]

key = b''
hex_charset = b'0123456789abcdef'
for i in range(64):
    possible_key_bytes = set(list(range(256)))
    for enc_secret in enc_secrets:
        possible_key_bytes &= set(
            [enc_secret[i] ^ hex_charset[j] for j in range(16)])

    if len(possible_key_bytes) == 1:
        key += bytes([possible_key_bytes.pop()])
    else:
        print(f"Error: Found multiple possible key bytes({
              len(possible_key_bytes)}) for position {i}")

secret = xor(final_secret, key)

io.sendlineafter(b"Please enter the secret code: ", secret)


io.recvline()

flag = io.recvline().decode().strip()
flag = flag.split(": ")[-1]

print(flag)
