"""
    CryptoPals - Set 2
    Challenge 10: Implement CBC mode
"""
from Crypto.Cipher import AES
from base64 import b64decode
from pwn import xor

from ..Func.aes_ecb_dec import aes_ecb_decrypt
from ..Func.pad7 import strip_pkcs7

BLOCK_SIZE = AES.block_size

def aes_cbc_decrypt(key, ciphertext, iv):
    # Split the ciphertext into blocks with given BLOCK_SIZE
    blocks = [ ciphertext[(BLOCK_SIZE*i):(BLOCK_SIZE*(i+1))] for i in range(int(len(ciphertext)//BLOCK_SIZE)) ]
    previous_ct = iv
    plaintext = b""
    for block in blocks:
        output = aes_ecb_decrypt(key, block)
        plaintext += xor(previous_ct, output)
        previous_ct = block
    plaintext = strip_pkcs7(plaintext)
    return plaintext



if __name__ == "__main__":
    with open("./CryptoPals/Set2/10.txt") as file:
        data_b64 = file.read()
    ciphertext = b64decode(data_b64)
    key = b"YELLOW SUBMARINE"
    iv = bytes(BLOCK_SIZE)
    plaintext = aes_cbc_decrypt(key, ciphertext, iv)
    print(plaintext.decode("ascii"))

# done
# Reference: https://www.youtube.com/watch?v=dUxCEePzhxw&list=PLWvDpnCcem1P6i8pZm2x7KHp5iaxwrK_P&index=12