from os import urandom
from random import choice, randint
from typing import Callable

from Crypto.Cipher import AES

from ..Func.pad7 import pkcs7

EncOracleType = Callable[[bytes], bytes] # takes one bytestring argument, return bytes

BLOCK_SIZE = AES.block_size
KEY_SIZE = 16

def get_encryption_oracle() -> tuple[str, EncOracleType]:
    mode = choice(("ECB", "CBC"))
    
    def encryption_oracle(plaintext: bytes) -> bytes:
        key = urandom(KEY_SIZE)
        prefix = urandom(randint(5, 10))
        postfix = urandom(randint(5, 10))
        # print(len(prefix), len(postfix))
        plaintext = pkcs7(prefix + plaintext + postfix)
        # print(plaintext)
        if mode == "ECB":
            cipher = AES.new(key, AES.MODE_ECB)
        else:
            iv = urandom(BLOCK_SIZE)
            cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.encrypt(plaintext)
    
    return mode, encryption_oracle

def detector(func: EncOracleType) -> str:
    plaintext = bytes(2*BLOCK_SIZE + (BLOCK_SIZE - 5))
    ciphertext = func(plaintext)
    # print(len(ciphertext))
    ct_blocks = [ ciphertext[(BLOCK_SIZE*i):(BLOCK_SIZE*(i+1))] for i in range(int(len(ciphertext)//BLOCK_SIZE)) ]
    # print(ct_blocks)
    if ct_blocks[1] == ct_blocks[2]:
        return "ECB"
    else:
        return "CBC"

if __name__ == "__main__":
    for _ in range(10):
        _mode, oracle = get_encryption_oracle()
        guess = detector(oracle)
        print("Actual: ", _mode, "Guessed:", guess)
        if _mode != guess:
            raise Exception("Oh no!")
    print("It worked!")