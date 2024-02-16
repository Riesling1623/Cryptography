"""
    CryptoPals - Set 2
    Challenge 15: PKCS#7 padding validation
"""

from ..Func.pad7 import *

from Crypto.Cipher import AES

BLOCK_SIZE = AES.block_size

def check_valid_padding(padding_pt: bytes, block_size = BLOCK_SIZE) -> bool:
    if len(padding_pt) % block_size == 0:
        padding_len = padding_pt[-1]
        if padding_len <= block_size:
            check = bytes([padding_len] * padding_len)
            if check == padding_pt[-1*padding_len:]:
                return True
            raise Exception("Invalid: Not PKCS#7 padding.")
        raise Exception("Invalid: The plaintext has no padding.")
    raise Exception("Invalid: The plaintext with padding must be multiple by block size.")

if __name__ == "__main__":
    plaintext = b"ICE ICE BABY\x04\x04\x04\x04"
    checked = check_valid_padding(plaintext)
    if checked == True:
        res = strip_pkcs7(plaintext)
    print(res)

# done