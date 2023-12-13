"""
    CryptoHack - Public key Cryptography
    RSA Starter 2 Solution
"""

# Encrypt the number 12 using the exponent e = 65537 and the primes p = 17 and q = 23.
e = 65537
p = 17
q = 23

# From 2 prime numbers p and q, we can calculate the modulus N.
N = p * q

# ciphertext
print(pow(12, e, N))