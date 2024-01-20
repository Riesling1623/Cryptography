"""
    CryptoPals - Set 1
    Challenge 7: AES in ECB mode Solution using pycryptodome
"""

from base64 import b64decode
from Crypto.Cipher import AES

def aes_ecb_decrypt(key: bytes, ciphertext: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

if __name__ == '__main__':
    with open("./CryptoPals/Set1/7.txt") as file:
        data_b64 = file.read()
    
    ciphertext = b64decode(data_b64)
    plaintext = aes_ecb_decrypt(b'YELLOW SUBMARINE', ciphertext)

    print(f"{plaintext = }")