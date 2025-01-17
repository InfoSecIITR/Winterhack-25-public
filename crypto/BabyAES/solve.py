from pwn import *

io = process(["python3","chall.py"], level='debug')


# Level 1
io.recvuntil(b"Here's your encrypted secret: ")
enc_secret = io.recvline().decode().strip()
blocks = [enc_secret[i:i+32] for i in range(0, len(enc_secret), 32)]
blocks = blocks[1:] + [blocks[0]]
modified_enc_secret = ''.join(blocks)

io.sendlineafter(b"Enter a message to be decrypted: ",
                 modified_enc_secret.encode())
io.recvuntil(b"Here is your decrypted message: ")

dec_secret = io.recvline().decode().strip()
dec_secret = dec_secret
dec_secret_blocks = [dec_secret[i:i+32] for i in range(0, len(dec_secret), 32)]
original_secret_blocks = [dec_secret_blocks[-1]] + dec_secret_blocks[:-1]
original_secret = ''.join(original_secret_blocks)

io.sendlineafter(b"Please enter the secret code: ", original_secret.encode())

# Level 2
io.recvuntil(b"Here's your encrypted message: ")
enc = io.recvline().decode().strip()
iv = bytes.fromhex(enc[:32])
enc = enc[32:]

msg = b'winner=false'
target_msg = b'winner=true'

target_iv = xor(iv, xor(msg, target_msg))
target_iv = target_iv.hex()

io.sendlineafter(b"Enter a message to be decrypted: ",
                 (target_iv + enc).encode())

io.interactive()
