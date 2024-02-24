from time import time
from random import randint

from ..Func.some_func import html_test, MT19937_32

now = int(time())
delta1 = randint(40, 1000)
seed = now  + delta1
delta2 = randint(40, 1000)
prng = MT19937_32(seed)

random_nb = next(prng)
time_of_output = now + delta1 + delta2

for i in range(40, 1000):
    seed = time_of_output - i
    prng = MT19937_32(seed)
    if next(prng) == random_nb:
        guess = seed
        break
else:
    raise Exception('could not regenerate random nb')

html_test(guess == seed)