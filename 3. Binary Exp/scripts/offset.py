from pwn import *

p = process('./chall')
p.sendline(cyclic(200))
p.wait()
