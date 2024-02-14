st = "foo=bar&baz=qux&zap=zazzle"
lstEle = st.split("&")
# print(lstELe)
res = {}
for ele in lstEle:
    key, value = ele.split("=")
    res[key] = value
print(res)