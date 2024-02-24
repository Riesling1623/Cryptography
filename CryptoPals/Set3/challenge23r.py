from random import randint
from ..Func.some_func import html_test, MT19937_32

def MT_temper(x):
    (w, n, m, r) = (32, 624, 397, 31)
    a = 0x9908B0DF
    (u, d) = (11, 0xFFFFFFFF)
    (s, b) = (7, 0x9D2C5680)
    (t, c) = (15, 0xEFC60000)
    l = 18
    f = 1812433253
    
    y = x ^ ((x >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    return y ^ (y >> l)

# using a function that declares internal functions every time
# is not the most elegant thing to do,
# but it just felt wrong to create an object
# for something (untempering) that does not require any state
def untemper(y):
    (w, n, m, r) = (32, 624, 397, 31)
    a = 0x9908B0DF
    (u, d) = (11, 0xFFFFFFFF)
    (s, b) = (7, 0x9D2C5680)
    (t, c) = (15, 0xEFC60000)
    l = 18
    f = 1812433253

    def int_to_bit_list(x):
        return [int(b) for b in '{:032b}'.format(x)]

    def bit_list_to_int(l):
        return int(''.join(str(x) for x in l), base=2)

    def invert_shift_mask_xor(y, direction, shift, mask=0xFFFFFFFF):
        y = int_to_bit_list(y)
        mask = int_to_bit_list(mask)

        if direction == 'left':
            y.reverse()
            mask.reverse()
        else:
            assert direction == 'right'

        x = [None]*32
        for n in range(32):
            if n < shift:
                x[n] = y[n]
            else:
                x[n] = y[n] ^ (mask[n] & x[n-shift])

        if direction == 'left':
            x.reverse()

        return bit_list_to_int(x)

    xx = y
    xx = invert_shift_mask_xor(xx, direction='right', shift=l)
    xx = invert_shift_mask_xor(xx, direction='left', shift=t, mask=c)
    xx = invert_shift_mask_xor(xx, direction='left', shift=s, mask=b)
    xx = invert_shift_mask_xor(xx, direction='right', shift=u, mask=d)

    return xx

for _ in range(10):
    x = randint(0, 0xFFFFFFF)
    y = MT_temper(x)
    assert untemper(y) == x

html_test(True)

prng = MT19937_32()

state = [untemper(next(prng)) for _ in range(624)] 

cloned_prng = MT19937_32(state=state)

for _ in range(20):
    assert next(prng) == next(cloned_prng)

html_test(True)