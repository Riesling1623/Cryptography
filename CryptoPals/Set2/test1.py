from Crypto.Cipher import AES

BLOCK_SIZE = AES.block_size

bstr = b"ICE ICE BABYYYYY"

padding_len = bstr[-1]
print(padding_len)

# print(bstr[-1*padding_len:])

check = [padding_len] * padding_len
# print(bytes(check))

if len(bstr) % BLOCK_SIZE == 0:
    if bytes(check) == bstr[-1*padding_len:]:
        print("Valid")
    else:
        raise Exception("Invalid padding: Not PKCS#7 padding")
else:
    raise Exception("Invalid padding: The length of plaintext is not multiple by block size.")