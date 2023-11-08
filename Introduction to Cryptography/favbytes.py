from pwn import xor

st = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag = bytes.fromhex(st)

# the problem say that "I've hidden some data using XOR with a single byte". Pay attention to the keyword "single byte"
# A byte is a group of 8 bits. So there are 256 (2^8, using permutation in probability) possible values of single bytes 
# (from 00000000 to 11111111)

for singbyte in range(256):
    possible_flag = xor(singbyte, flag)
    if possible_flag[0:6] == b'crypto':
        print(possible_flag)
        break
