def xor13(i):
    return i^13

st = "label"
i = 13

lst = [ ord(c) for c in st ]
lstxor13 = [ xor13(i) for i in lst ]
lst_res = [ chr(i) for i in lstxor13 ]

print("".join(lst_res))