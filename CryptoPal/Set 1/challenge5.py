"""
    CryptoPal - Set 1
    Challenge 5: Implement repeating-key XOR Solution
"""

from pwn import xor

KEY = "ICE"
bytekey = bytes(KEY, 'utf-8')

with open('CryptoPal/Set 1/5.txt', 'r') as file:
    contents = file.read()
    bytecontents = bytes(contents, 'utf-8')
    # print(bytecontents)
    encrypted_string = xor(bytecontents, bytekey)
    print(encrypted_string.hex())
# done