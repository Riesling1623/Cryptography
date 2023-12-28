import struct
import binascii

TEST_STRING = u'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# print(type(TEST_STRING))
bytestring = binascii.unhexlify(TEST_STRING)
# print(type(bytestring))

test_string = [ struct.pack("B", byte) * len(bytestring) for byte in range(0,256) ]
for e in test_string:
    print(e)