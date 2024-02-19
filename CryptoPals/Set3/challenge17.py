"""
    CryptoPals - Set 3
    Challenge 17: The CBC padding oracle
"""

import random

from Crypto.Cipher import AES
from os import urandom
from base64 import b64decode

from ..Func.pad7 import pkcs7
from ..Set2.challenge15 import check_valid_padding

BLOCK_SIZE = AES.block_size
KEY_SIZE = 32
_key = urandom(KEY_SIZE)
iv = urandom(BLOCK_SIZE)

def first_func() -> bytes:
    # Select random one of 10 strings
    with open("./CryptoPals/Set3/17.txt") as f:
        lines = f.readlines()
    random_index = random.randint(0, 9)
    random_string = lines[random_index].strip()

    bpt = b64decode(random_string)
    bpt = pkcs7(bpt)
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    return cipher.encrypt(bpt)

def second_func(ciphertext: bytes) -> bool:
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return check_valid_padding(plaintext)

if __name__ == "__main__":
    ciphertext = first_func()
    checked = second_func(ciphertext)
    print(f"{checked=}")