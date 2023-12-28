"""
    CryptoPal - Set 1
    Challenge 2 - Fixed XOR Solution
"""

from pwn import xor

def xorCombine(s1, s2):
    # return xor(s1, s2)
    return xor(s1, s2).hex()

if __name__ == "__main__":
    s1 = "1c0111001f010100061a024b53535009181c"
    bs1 = bytes.fromhex(s1)
    s2 = "686974207468652062756c6c277320657965"
    bs2 = bytes.fromhex(s2)
    print(xorCombine(bs1, bs2))

# done