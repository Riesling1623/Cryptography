"""
    CryptoHack - Public key Cryptography
    Factoring solution
    
    This solution using the factordb module (can use sympy.factorint() but it is slower than this solution)
    Don't know how to install `primefac-fork`, which is provided by the challenge
"""
from factordb.factordb import FactorDB
num = 510143758735509025530880200653196460532653147

f = FactorDB(num)
f.connect()
print(f.get_factor_list())