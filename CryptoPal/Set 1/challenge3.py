"""
    CryptoPal - Set 1
    Challenge 3 - Single-byte XOR cipher Solution
"""

from pwn import xor
import string

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
bs = bytes.fromhex(hex_string)

for key in string.ascii_letters:
    bkey = bytes(key, 'utf-8')
    print(xor(bs, bkey))