"""
    CryptoPals - Set 1
    Challenge 4 - Detect single-character XOR Solution
"""

from challenge3_2 import englishness, single_byte_xor, find_single_byte_xor
from collections import Counter
from pwn import xor

import math
import struct

# Character frequency table of the English language
FREQUENCY_TABLE = {
    b'a':  0.08167,
    b'b':  0.01492,
    b'c':  0.02782,
    b'd':  0.04253,
    b'e':  0.1270,
    b'f':  0.02228,
    b'g':  0.02015,
    b'h':  0.06094,
    b'i':  0.06966,
    b'j':  0.00153,
    b'k':  0.00772,
    b'l':  0.04025,
    b'm':  0.02406,
    b'n':  0.06749,
    b'o':  0.07507,
    b'p':  0.01929,
    b'q':  0.00095,
    b'r':  0.05987,
    b's':  0.06327,
    b't':  0.09056,
    b'u':  0.02758,
    b'v':  0.00978,
    b'w':  0.02360,
    b'x':  0.00150,
    b'y':  0.01974,
    b'z':  0.00074,
}

# The table is useless in Python 3, where each individual string will be
# analysed as a byte. This code transforms it when necessary

if isinstance(b'a'[0], int):
    FREQUENCY_TABLE = {x[0]: y for x, y in FREQUENCY_TABLE.items()}

if __name__ == '__main__':
    res_lst = []
    with open('CryptoPals/Set1/4.txt', 'r') as file:
        for hex_line in file:
            bytestring = bytes.fromhex(hex_line)

            out = find_single_byte_xor(bytestring)
            res_lst.append(out)
    res_lst.sort(key=lambda x: x[0], reverse=True)
    res = res_lst[0]
    _, outcome, b = res

    print(res)
    print("Decoded string is {}".format(outcome.decode('ascii')))

# done