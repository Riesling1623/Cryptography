"""
    CryptoHack - Public key Cryptography
    RSA Starter 5 Solution
"""

# public key
N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
# ciphertext
c = 77578995801157823671636298847186723593814843845525223303932
# private key found in previous challenge
d = 121832886702415731577073962957377780195510499965398469843281

# plaintext
print(pow(c,d,N))