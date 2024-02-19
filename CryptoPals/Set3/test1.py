import struct

from base64 import b64decode
from Crypto.Cipher import AES
from pwn import xor

from ..Func.bytes_to_chunks import bytes_to_chunks

key = b"YELLOW SUBMARINE"

def aes_ctr_decrypt(ct, counter):
    cipher = AES.new(key, AES.MODE_ECB)
    keystream = cipher.encrypt(counter)
    return xor(ct, keystream) 

BLOCK_SIZE = AES.block_size
s = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
bct = b64decode(s)
chunks = bytes_to_chunks(bct, BLOCK_SIZE)

nonce = struct.pack("<Q", 0)
counter = 0
# byte_counter = struct.pack("<Q", 0)
# counter_block = nonce + byte_counter

# print(aes_ctr_decrypt(chunks[0], counter_block))
res_lst = []
for chunk in chunks:
    counter = chunks.index(chunk)
    byte_counter = struct.pack("<Q", counter)
    counter_block = nonce + byte_counter

    res_lst.append(aes_ctr_decrypt(chunk, counter_block)[:len(chunk)])

print(res_lst)
