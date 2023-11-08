from pwn import xor
from base64 import b64encode

st = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_st = bytes.fromhex(st)
for i in bytes_st:
    # print(chr(i).encode(), end=" ")
    print(b64encode(xor(bytes_st, chr(i).encode())))

print(bytes_st)