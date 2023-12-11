"""
    CryptoHack - Passwords as Keys
"""

from Crypto.Cipher import AES
import hashlib
import requests
import os

BASE_URL = "https://aes.cryptohack.org/passwords_as_keys/"

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    return decrypted

# Take the ciphertext
r = requests.get(f"{BASE_URL}encrypt_flag/")
data = r.json()
ciphertext = data["ciphertext"]
# print(ciphertext)

# Take the password hash
if not os.path.exists("Symmetric Cryptography/usr/share/dict/"):
    os.makedirs("Symmetric Cryptography/usr/share/dict/")
    os.chdir("Symmetric Cryptography/usr/share/dict/")
else:
    os.chdir("Symmetric Cryptography/usr/share/dict/")

r = requests.get("https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words")
if r.status_code == 200:
    with open("words.txt", "w", encoding="utf-8") as file:
        file.write(r.text)

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

# Take the plaintext
for w in words:
    KEY = hashlib.md5(w.encode()).digest()
    possible_flag = decrypt(ciphertext, KEY)
    if b'crypto' in possible_flag:
        print(possible_flag)
        break
