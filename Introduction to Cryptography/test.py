from pwn import xor

st = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag = bytes.fromhex(st)

for singbyte in range(256):
    possible_flag = xor(singbyte, flag)
    if possible_flag[0:6] == b'crypto':
        print(True)
        break
