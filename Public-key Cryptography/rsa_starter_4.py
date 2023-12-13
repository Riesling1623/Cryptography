"""
    CyptoHack - Public key Cryptography
    RSA Starter 4 Solution
    Using the extended Euclidean algorithm
"""

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
totient = (p-1)*(q-1)

# private key
print(egcd(e, totient))