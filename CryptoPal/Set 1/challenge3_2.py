"""
    CryptoPals - Set 1
    Challenge 3 - Another solution using scoring English frequency.
"""

import math
import struct

from collections import Counter
from pwn import xor

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

def englishness(a):
    """
    This function determines how 'likely' a string is to be English, based on
    character frequency. Returns a value between 0 and 1, where 0 means
    'totally unlike English', and 1 means 'exactly like English'

    Applying the 'Bhattacharyya Coefficient': For each point in the
    distribution, multiply the probability for rach distribution together,
    take the square root, then sum all the probabilities together to get
    coefficient

    Reference: https://en.wikipedia.org/wiki/Bhattacharyya_distance
    """

    # Use the Counter dictionary to find out how often each character appears
    # as a sum total.
    c = Counter(a.lower())
    total_characters = len(a)

    # Applying the Bhattancharyya Coefficient like above
    # If any element is entirely absent then the frequency is zero: this
    # penalises punctuation heavily
    coefficient = sum(
        math.sqrt(FREQUENCY_TABLE.get(char, 0) * y/total_characters)
        for char, y in c.items()   
    )

    return coefficient

def single_byte_xor(st, b):
    """
    Given a byte, XORs all characters in a byte string with that byte and
    returns it
    """
    test_string = struct.pack("B", b) * len(st)
    return xor(st, test_string)

def find_single_byte_xor(st):
    results = ((single_byte_xor(st, b), b) for b in range(0, 256))
    emap = [(englishness(r[0]), r[0], r[1]) for r in results]

    emap.sort(key=lambda x: x[0], reverse=True)
    res = emap[0]
    return res

if __name__ == '__main__':
    HEX_STRING = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    bytestring = bytes.fromhex(HEX_STRING)

    res = find_single_byte_xor(bytestring)
    print(res)

# Reference for this solution: https://github.com/Lukasa/cryptopals/blob/master/cryptopals/challenge_one/three.py