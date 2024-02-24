"""
    CryptoPals - Set 3
    Challenge 18: Implement CTR, the stream cipher mode
"""

import struct

from base64 import b64decode
from Crypto.Cipher import AES
from pwn import xor

from ..Func.bytes_to_chunks import bytes_to_chunks

_key = b"YELLOW SUBMARINE"
BLOCK_SIZE = AES.block_size

def aes_ctr_transform(data: bytes, key: bytes, nonce = 0, counter = 0):
    res = b""
    # little endian
    chunks = bytes_to_chunks(data, BLOCK_SIZE)
    nonce = struct.pack("<Q", nonce)
    counter_byte = struct.pack("<Q", counter)
    counter_block = nonce + counter_byte

    cipher = AES.new(key, AES.MODE_ECB)

    for chunk in chunks:
        keystream = cipher.encrypt(counter_block)
        res += xor(chunk, keystream)[:len(chunk)]
        counter += 1
        counter_byte = struct.pack("<Q",counter)
        counter_block = nonce + counter_byte
    return res

if __name__ == "__main__":
    ct = b64decode(
        "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
    )
    nonce = 0
    counter = 0
    res = aes_ctr_transform(ct, _key, nonce, counter)
    print(res)
