from base64 import b64decode
from itertools import islice

import os

from ..Func.some_func import *

with open("./CryptoPals/Set4/25.txt") as f:
    data = b64decode(f.read())

key = os.urandom(16)
nonce = 0

ctxt = transform_aes_128_ctr(data, key, nonce)

def edit(ctxt, key, nonce, offset, newtext):
    keystream = aes_128_ctr_keystream_generator(key, nonce)

    new_chunk = bxor(newtext, islice(keystream, offset, offset+len(newtext)))

    result = ctxt[:offset] + new_chunk + ctxt[offset+len(newtext):]
    return result

edited_ctxt = edit(ctxt, key, nonce,
                  offset=10, newtext=b'LOOOOOL')

print(data[:20])
print(transform_aes_128_ctr(edited_ctxt, key, nonce)[:20])

recovered_keystream = edit(ctxt, key, nonce,
                           offset=0,
                           newtext=b'\x00'*len(ctxt))

recovered_plaintext = bxor(ctxt, recovered_keystream)
html_test(recovered_plaintext == data)