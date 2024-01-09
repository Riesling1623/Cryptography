from pwn import xor
from base64 import b64decode

with open('./CryptoPals/Set 1/6.txt') as file:
    ciphertext = file.read()
ciphertext = b64decode(ciphertext)
# print(ciphertext)

# key = "TERMINATOR\0X→\0BRING\0THE\0NOISE"
key = "84 69 82 77 73 78 65 84 79 82 0 88 26 0 66 82 73 78 71 0 84 72 69 0 78 79 73 83 69"
keylist = key.split(" ")
keylist = [chr(int(x)) for x in keylist]
# print("".join(keylist))
key = "".join(keylist)

# print(len(key))
bytekey = bytes(key, 'utf-8')
# print((bytekey))s

# print(xor(ciphertext, bytekey))
res_byte = xor(ciphertext, bytekey)
res = res_byte.decode('utf-8')
print(res)

# Maybe done :)