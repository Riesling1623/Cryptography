# ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'
ciphertext = b'abcdef'
key = b'ab'

block_ciphertexts = [ ciphertext[len(key)*i:len(key)*(i+1)] for i in range(int(len(ciphertext)/len(key))) ]
print(block_ciphertexts)