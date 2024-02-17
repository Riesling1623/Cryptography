"""
    CryptoPals - Set 2
    Challenge 16: CBC bitflipping attacks
"""

from Crypto.Cipher import AES
from os import urandom
from pwn import xor

from ..Func.pad7 import *
from ..Func.bytes_to_chunks import bytes_to_chunks

# Generate a random AES key
KEY_SIZE = 32
BLOCK_SIZE = AES.block_size
_key = urandom(KEY_SIZE)
iv = urandom(BLOCK_SIZE)

def quote_out_character(bstr: bytes):
    return bstr.replace(b"=", b"%3D").replace(b";", b"%3B")

def first_func(bstr: bytes) -> bytes:
    prefix = b"comment1=cooking%20MCs;userdata="
    postfix = b";comment2=%20like%20a%20pound%20of%20bacon"
    bstr = quote_out_character(bstr)
    # return prefix + bstr + postfix
    plaintext = prefix + bstr + postfix
    plaintext = pkcs7(plaintext)
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    return cipher.encrypt(plaintext)

def second_func(ciphertext: bytes) -> bool:
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = strip_pkcs7(plaintext)
    print(f"{plaintext=}")
    if b";admin=true;" in plaintext:
        return True
    return False

def make_admin():
    a_block = b"A" * BLOCK_SIZE
    ct = first_func(a_block * 2)
    # print(f"{ct=}")
    ct_blocks = bytes_to_chunks(ct, BLOCK_SIZE)
    # print(f"{ct_blocks=}")
    flipper = xor(a_block, b";admin=true".rjust(BLOCK_SIZE, b"A"))
    # print(f"{flipper=}")
    ct_blocks[2] = xor(ct_blocks[2], flipper)
    return b"".join(ct_blocks)

if __name__ == "__main__":
    ct_chosen = make_admin()
    # print(f"{ct_chosen=}")

    print("Check admin:", second_func(ct_chosen))

# done
# Reference: https://www.youtube.com/watch?v=Q6wopwjhyig&list=PLWvDpnCcem1P6i8pZm2x7KHp5iaxwrK_P&index=16