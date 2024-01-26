"""
    CryptoPals - Set 2
    Challenge 11: An ECB/CBC detection oracle
"""

import os

from random import randint
from Crypto.Cipher import AES
from ..Func.pad7 import pkcs7

BLOCK_SIZE = AES.block_size
# KEY_SIZE can be equal to 128, 256, or 512 bits. The larger the size, the higher the safety, 
# in return, the longer the calculation time will be
KEY_SIZE = 32

# Using os.urandom(size) to generate a random AES key.
def gen_rand_key(size: int = BLOCK_SIZE) -> bytes:
    return os.urandom(size)

def append_pt(input_data: bytes):
    append_size_1 = randint(5, 10)
    append_size_2 = randint(5, 10)
    return os.urandom(append_size_1) + input_data + os.urandom(append_size_2)

def encryptOracle(input_data: bytes) -> tuple[str, bytes]:
    # append to the plaintext
    pt = append_pt(input_data)
    plaintext = pkcs7(pt)
    
    # generate random key
    key = gen_rand_key()

    # Suppose that 0 is ECB and 1 is CBC.
    choice = randint(0, 1)
    if choice == 0:
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        return ("ECB",ciphertext)
    else:
        # iv will be automately created in cipher
        # iv = os.urandom(BLOCK_SIZE)
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(plaintext)
        return ("CBC", ciphertext)

def detectOracle() -> tuple[str, str]: 
    """
        To be able to detect when oracle is using ECB mode, when is using CBC mode, I need to take advantage of ECB's weaknesses. So I need
        2 blocks with identical content in plaintext (32 bytes). For prefix and postfix between 5 and 10, I would choose both equal to 10,
        since if not divisible by BLOCK_SIZE then there is still padding with pkcs7. So after prefix I need 5 bytes and
        before postfix I need 4 bytes (so padding won't create 1 whole new blocks) 
    """
    plaintext = bytes(2*BLOCK_SIZE + (6+5))
    encrypted_pt = encryptOracle(plaintext)
    mode = encrypted_pt[0]
    ciphertext = encrypted_pt[1]
    blocks = [ ciphertext[(BLOCK_SIZE*i):(BLOCK_SIZE*(i+1))] for i in range(int(len(ciphertext)//BLOCK_SIZE)) ]
    if (blocks[1] == blocks[2]):
        return (mode, "ECB")
    else:
        return (mode, "CBC")
    


if __name__ == "__main__":
    for _ in range(10):
        detect = detectOracle()
        print("Actual:", detect[0], "& Detect:", detect[1])
        if detect[0] != detect[1]:
            print("Something wrong")
            break

# done
# Referenced by: https://www.youtube.com/watch?v=i6BhbO_g4KI&list=PLWvDpnCcem1P6i8pZm2x7KHp5iaxwrK_P&index=12