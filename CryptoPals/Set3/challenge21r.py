import json

from ..Func.some_func import html_test

def MT19937_32(seed=5489):
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