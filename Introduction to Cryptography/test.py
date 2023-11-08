from pwn import xor

ciphertext = "5d41402abc4b2a76b9719d911017c592"
key = "secret"

print(bytes.fromhex(ciphertext))
xored = xor(bytes.fromhex(ciphertext), key.encode())
print(xored)