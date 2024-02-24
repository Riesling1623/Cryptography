from os import urandom
from base64 import b64decode
from ..Func.some_func import transform_aes_128_ctr, attack_single_byte_xor

with open("./CryptoPals/Set3/20.txt") as f:
    data = [b64decode(line) for line in f]

key = urandom(16)

ctxts = [transform_aes_128_ctr(line, key, nonce=0) for line in data]
# print(ctxts)

# Python has a very useful "zip" builtin function
# that perfectly fits our need here
# let's just first show how it works
# note that the 'zip' function stop at the length of the shortest input
tmp = list(zip('abc', 'def', 'ghijkl'))
# print(tmp)

# the 'next' builtin function will take the first element outputed by the zip function
# (zip is actually an Python iterator)
# the '*' operator before ctxt will unpack the elements of the 'ctxt' variable
# as multiple arguments of the function (see how we called zip in the previous cell)
l = next(zip(*ctxts))

# print(list(zip(*ctxts)))

tmp1 = attack_single_byte_xor(l)
# print(tmp1)

columns = [ attack_single_byte_xor(l)['message'] for l in zip(*ctxts) ]
# print(columns)
for msg in zip(*columns):
    print(bytes(msg).decode())