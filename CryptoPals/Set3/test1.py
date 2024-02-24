# challenge 20

from .challenge18 import aes_ctr_transform
from ..Func.some_func import attack_single_byte_xor
from Crypto.Cipher import AES
from os import urandom
from base64 import b64decode

BLOCK_SIZE = AES.block_size
KEY_SIZE = 32
_key = urandom(KEY_SIZE)
nonce = 0

with open("./CryptoPals/Set3/20.txt") as f:
    data = [b64decode(line) for line in f]

# print(data)

# encrypt
ctxts = [aes_ctr_transform(ele, _key) for ele in data]
# print(ctxts)

cols = [attack_single_byte_xor(l)['message'] for l in zip(*ctxts)]
for pt in zip(*cols):
    print(bytes(pt).decode())