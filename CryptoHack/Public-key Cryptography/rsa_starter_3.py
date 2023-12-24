"""
    CryptoHack - Public key Cryptography
    RSA Starter 3 Solution
"""

p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# Find the totient of N
# Because p and q are prime numbers
totient = (p-1)*(q-1)
print(totient)