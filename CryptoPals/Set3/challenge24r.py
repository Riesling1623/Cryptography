import os

from math import log2
from ..Func.some_func import MT19937_32, html_test
from random import randint
from time import time

def mt19937_keystream_generator(key):
    assert log2(key) <= 16
    prng = MT19937_32(key)
    while True:
        rand_nb = next(prng)
        # 32 bits = 4 bytes
        yield from rand_nb.to_bytes(4, byteorder='big')

def transform_mt19937(msg, key):
    assert isinstance(key, int)
    keystream = mt19937_keystream_generator(key)
    
    return bytes([ x^y for (x,y) in zip(msg, keystream)])

key = 1234
ctxt = transform_mt19937(b'hello there!', key)
print(ctxt)
print(transform_mt19937(ctxt, key))

MAX_SEED = (1<<16) - 1

key = randint(1, MAX_SEED)

prefix_size = randint(2,20)
prefix = os.urandom(prefix_size)

ctxt = transform_mt19937(prefix + b'A'*14, key)

for i in range(1, MAX_SEED):
    p = transform_mt19937(ctxt, i)
    if p.endswith(b'A'*14):
        result = i
        break
else:
    html_test(False)
    
# html_test(result==key)

def gen_token():
    seed = int(time()) & MAX_SEED
    pseudo_random_byte_gen = mt19937_keystream_generator(seed)
    token = bytes(next(pseudo_random_byte_gen) for _ in range(16))
    return token

token = gen_token()

def is_generated_with_mt19937(token):
    for i in range(1, MAX_SEED):
        pseudo_random_byte_gen = mt19937_keystream_generator(i)
        guess = bytes(next(pseudo_random_byte_gen) for _ in range(16))
        if guess == token:
            return True
    else:
        return False

assert is_generated_with_mt19937(token)
assert not is_generated_with_mt19937(os.urandom(16))
html_test(True)