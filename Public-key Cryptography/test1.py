from factordb.factordb import FactorDB

f = FactorDB(16)
f.connect()
print(f.get_factor_list())
print(f.get_factor_from_api())