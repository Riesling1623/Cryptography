"""
Cryptohack - Block Cipher Mode Starter
Solution using the requests Python module

Ref:
    https://docs.python-requests.org/en/master/user/quickstart
    https://cryptohack.org/challenges/block_cipher_starter/solutions/
"""

import requests

BASE_URL = "https://aes.cryptohack.org/block_cipher_starter/"

# Get the ciphertext of the encrypted flag

r = requests.get(f"{BASE_URL}/encrypt_flag/")
# `print(r.text)` the same as `print(data)`
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext:", ciphertext)

# Send the ciphertext to the decrypt function
r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("plaintext:", plaintext)

# Convert from HEX to bytes to have a flag
flag = bytes.fromhex(plaintext)
print(flag)