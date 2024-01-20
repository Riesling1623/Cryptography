from base64 import b64decode
from EditDistance import editDistance
from challenge3_2 import find_single_byte_xor, single_byte_xor

def check_printable(byteval):
    for byte in byteval:
        if byte < 32 or byte > 126:
            return False
    return True

def convert_to_binary(b):
    return "".join("{:08b}".format(x) for x in b)

with open("./CryptoPals/Set 1/6.txt") as file:
    ciphertext = file.read()
# print(b64decode(ciphertext))
ciphertext = b64decode(ciphertext)

keysize_dict = {}

for size in range(2, 41):
    # first = convert_to_binary(ciphertext[:size])
    # second = convert_to_binary(ciphertext[size:(2*size)])
    blockkey = [ciphertext[:size], ciphertext[size:(2*size)], ciphertext[(2*size):(3*size)]]
    # keysize_dict[size] = editDistance(first, second)/size
    # print(blockkey)
    ham_distance = [editDistance(blockkey[i], blockkey[i+1])/size for i in range(len(blockkey) - 1)]
    avg_ham_distance = sum(ham_distance)/len(ham_distance)
    keysize_dict[size] = avg_ham_distance
    # print(avg_ham_distance)
    # break

sorted_keydict = dict(sorted(keysize_dict.items(), key=lambda item: item[1]))
# print(sorted_keydict)

# Assume that key size is 5, 11, 29 => See 29 maybe the keysize
keysize = 29
count = 0

blocks = [ ciphertext[i::keysize] for i in range(keysize) ]
# print(len(blocks))

for i in range(len(blocks)):
    res_block = find_single_byte_xor(blocks[i])
    print((res_block[2]), end=" ")

#     res = [(single_byte_xor(blocks[i], b), i, b) for b in range(0, 256)]
#     # print(res)
#     for val in res:
#         # print(type(val[0]))
#         if check_printable(val[0]) == True:
#             print(val)
#             count += 1
# print(count)

# TERMINATOR X→ BRING THE NOISE