from pwn import xor
a = [206, 243]
b = [173, 129]
res = [ xor(a[i],b[i]).decode() for i in range(len(a)) ]
print("".join(res))