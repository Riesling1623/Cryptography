"""
    CryptoPals - Set 2
    Challenge 13: ECB cut-and-paste
"""

from ..Func.pad7 import pkcs7, strip_pkcs7

from Crypto.Cipher import AES
from os import urandom

KEY_SIZE = 32
_key = urandom(KEY_SIZE)

def parse_profile(profile_string: bytes) -> dict:
    # Parses a structured profile string into a dictionary.
    lstEle = profile_string.split(b'&')
    res = {}
    for ele in lstEle:
        key, value = ele.split(b'=')
        res[key] = value
    return res

def profile_for(email: bytes) -> bytes:
    if b'&' in email or b'=' in email:
        raise Exception("Invalid email")
    d = {}
    d[b"email"] = email
    d[b"uid"] = b"10"
    d[b"role"] = b"user"
    
    pairs = []
    for key, value in d.items():
        pairs.append(key + b"=" + value)
    return b"&".join(pairs)

def encProfile(email: bytes) -> bytes:
    cipher = AES.new(_key, AES.MODE_ECB)
    profile = profile_for(email)
    return cipher.encrypt(pkcs7(profile))

def decProfile(profile: bytes) -> bytes:
    cipher = AES.new(_key, AES.MODE_ECB)
    return strip_pkcs7(cipher.decrypt(profile))


def visualAttack():
    email1 = b"foooo@bar.com"
    email2 = email1[:10] + pkcs7(b"admin") + email1[10:]
    
    encrypted_email1 = encProfile(email1)
    encrypted_email2 = encProfile(email2)
    
    return encrypted_email1[:32] + encrypted_email2[16:32] 

if __name__ == "__main__":
    encrypted_email = visualAttack()
    decrypted = decProfile(encrypted_email)
    print(decrypted)

# done