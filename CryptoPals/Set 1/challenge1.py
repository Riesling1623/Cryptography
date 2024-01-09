"""
    CryptoPal - Set 1
    Challenge 1 - Convert hex to base64 Solution
"""

from base64 import b64encode

# The string
s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

byte_s = bytes.fromhex(s) # Hex to bytes
res = b64encode(byte_s) # Bytes to base64

print(res)

# done