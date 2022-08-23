from pwn import *

string = "label"
def xor():
    return xor(b'string', 13)

xor()

print(string)