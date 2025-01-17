from pwn import *
from math import ceil

query_count = 0
block_size = 16
io = process(["python3", "chall.py"])


def level1_oracle(msg: bytes) -> bytes:
    global query_count

    query_count += 1
    io.sendlineafter(b"[cmd]", b"encrypt")
    io.sendlineafter(b"Enter a message to be encrypted: ", msg.hex().encode())

    enc = io.recvline().decode().strip()
    enc = enc.split(": ")[-1]
    enc = bytes.fromhex(enc)

    return enc


prefix_len = len(b"All the very best! I hope you solve this challenge.")
initial_padding = block_size - (prefix_len % block_size)
skip_blocks = ceil(prefix_len/block_size)
enc = level1_oracle(b"")

secret_blocks = ceil((len(enc) - prefix_len)/block_size)
secret = b""
recovered = False
prev_block = b"\x00"*16


while True:
    target_block_idx = skip_blocks + len(secret) // block_size
    cur_block = b""

    for j in range(block_size - 1, -1, -1):
        msg = b"\x00" * initial_padding + b"\x00"*j

        enc = level1_oracle(msg)
        target_block = enc[target_block_idx *
                           block_size: (target_block_idx+1) * block_size]

        for b in range(256):
            msg = b"\x00"*initial_padding + \
                prev_block[(block_size - j):] + cur_block + bytes([b])

            enc = level1_oracle(msg)
            block = enc[skip_blocks *
                        block_size: (skip_blocks + 1) * block_size]

            if block == target_block:
                cur_block += bytes([b])
                break
        else:
            cur_block = cur_block[:-1]
            recovered = True
            break

    secret += cur_block
    prev_block = cur_block

    if recovered:
        break

io.sendlineafter(b"[cmd]", b"secret")
io.sendlineafter(b"Enter the secret code: ", secret.hex().encode())


# Level 2
io.recvlines(2)


def level2_oracle(query):
    global query_count
    query_count += 1
    assert len(query) % block_size == 0
    io.sendlineafter(b": ", query.hex().encode())
    response = io.recvline().decode()
    return "Invalid" not in response


def get_iv(block: bytes, target_msg: bytes) -> bytes:
    cur_iv = b"\x00"*block_size

    for i in range(block_size):
        for b in range(256):
            iv = cur_iv[:i] + bytes([b]) + cur_iv[i+1:]
            msg = iv + block
            resp = level2_oracle(msg)
            if resp:
                cur_iv = iv
                if i == block_size - 1:
                    break

                cur_iv = xor(
                    xor(cur_iv[:(i+1)], bytes([i+1])*(i+1)), bytes([i+2])*(i+1)) + cur_iv[i+1:]
                break
        else:
            raise Exception("Something went wrong!")

    cur_iv = xor(cur_iv, target_msg)
    cur_iv = xor(cur_iv, bytes([block_size]) * block_size)
    return cur_iv


msg = b"Please give me the flag."
padding = block_size - (len(msg) % block_size)
msg = bytes([padding])*padding + msg

msg_blocks = [msg[i:i+block_size] for i in range(0, len(msg), block_size)]

prev_block = b"\x00"*block_size

blocks = [prev_block]

for i in range(len(msg_blocks) - 1, -1, -1):
    iv = get_iv(prev_block, msg_blocks[i])
    prev_block = iv
    blocks = [iv] + blocks

final_message = b"".join(blocks)
io.sendlineafter(b": ", final_message.hex())

io.recvline()

flag = io.recvline().decode().strip()
flag = flag.split(": ")[-1]

log.critical(f"query_count: {query_count}")
io.close()

print(flag)
