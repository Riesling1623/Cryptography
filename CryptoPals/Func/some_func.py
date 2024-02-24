from Crypto.Cipher import AES
from itertools import zip_longest
from math import ceil

import IPython.display

_HTML_INFO_STYLE = ( 'border:1px solid #c3e6cb;'
   'padding:.75rem 3rem;'
   'border-radius:.5rem;'
   'font-weight:bold;'
   'text-align: center;'
)

def html_test(condition):
    if condition:
        html = IPython.display.HTML(
            '<div style="' +
            _HTML_INFO_STYLE +
            'background-color:#d4edda;'
            'color:#155724;'
            'border-color:#c3e6cb;'
            '">OK</div>')
    else:
        html = IPython.display.HTML(
            '<div style="' +
            _HTML_INFO_STYLE +
            'background-color:#f8d7da;'
            'color:#721c24;'
            'border-color:#f5c6cb;'
            '">ERROR</div>')

    IPython.display.display(html)

def MT19937_32(seed=5489, state=None):
    '''Mersenne-Twister PRNG, 32-bit version'''
    # parameters for MT19937-32
    (w, n, m, r) = (32, 624, 397, 31)
    a = 0x9908B0DF
    (u, d) = (11, 0xFFFFFFFF)
    (s, b) = (7, 0x9D2C5680)
    (t, c) = (15, 0xEFC60000)
    l = 18
    f = 1812433253

    # masks (to apply with an '&' operator)
    # ---------------------------------------
    # zeroes out all bits except "the w-r highest bits"
    # (i.e. with our parameters the single highest bit, since w-r=1)
    high_mask = ((1<<w) - 1) - ((1<<r) - 1)
    # zeroes out all bits excepts "the r lowest bits"
    low_mask = (1<<r)-1

    def twist(x):
        return (x >> 1)^a if (x % 2 == 1) else x >> 1

    if state == None:
        # initialization (populating the state)
        state = list()
        state.append(seed)
        for i in range(1, n):
            prev = state[-1]
            # the "& d" is to take only the lowest 32 bits of the result
            x = (f * (prev ^ (prev >> (w-2))) + i) & d
            state.append(x)

    while True:
        x = state[m] ^ twist((state[0] & high_mask) + (state[1] & low_mask))

        # tempering transform and output
        y = x ^ ((x >> u) & d)
        y = y ^ ((y << s) & b)
        y = y ^ ((y << t) & c)
        yield y ^ (y >> l)

        # note that it's the 'x' value
        # that we insert in the state
        state.pop(0)
        state.append(x)


def bxor(a, b, longest=True):
    if longest:
        return bytes([ x^y for (x,y) in zip_longest(a,b,fillvalue=0) ])
    else:
        return bytes([ x^y for (x,y) in zip(a,b) ])

def encrypt_aes_128_block(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)

def aes_128_ctr_keystream_generator(key, nonce):
    counter = 0
    while True:
        to_encrypt = (nonce.to_bytes(length=8, byteorder="little") + counter.to_bytes(length=8, byteorder="little"))
        keystream_block = encrypt_aes_128_block(to_encrypt, key)
        # equivalent to "for byte in keystream_block: yield byte"
        # for the "yield" keyword in Python
        yield from keystream_block

        counter += 1

def transform_aes_128_ctr(msg, key, nonce):
    """
        Does both encryption and decryption
    """
    keystream = aes_128_ctr_keystream_generator(key, nonce)
    return bxor(msg, keystream, longest=False)

# bytes representing lowercase english letters and space
ascii_text_chars = list(range(97, 122)) + [32]

def attack_single_byte_xor(ciphertext):
    # a variable to keep track of the best candidate so far
    best = None
    for i in range(2**8):
        # for every possibly key
        # converting the key from a number to a byte
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(ciphertext)
        candidate_message = bxor(ciphertext, keystream)
        nb_letters = sum([ x in ascii_text_chars for x in candidate_message ])
        # if the obtained message has more letters than any other candidate before
        if best == None or nb_letters > best['nb_letters']:
            # store the current key and message as our best candidate so far
            best = {"message": candidate_message, 'nb_letters': nb_letters, 'key': candidate_key}
    return best

def split_bytes_in_blocks(x, blocksize):
    nb_blocks = ceil(len(x)/blocksize)
    return [x[blocksize*i:blocksize*(i+1)] for i in range(nb_blocks)]