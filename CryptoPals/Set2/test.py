from pwn import xor
from .test1 import first_func

a_block = b"A" * 16
ct = first_func(a_block)
print(f"{ct=}\n")
print(len(ct))

tmp = b";admin=true".rjust(16, b"A")
flipper = xor(a_block, tmp)
print(f"{flipper=}\n")

# print(f"{flipper=}")
padded = flipper.rjust(16 * 3, b"\x00").ljust(len(ct), b"\x00")
print(f"{padded=}\n")