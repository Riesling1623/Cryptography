from base64 import b64encode

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
# decode hex string into bytes
byte_res = bytes.fromhex(hex_string)
print(byte_res)

# Use `base64.b64encode(str)`
res = b64encode(byte_res)

print(res)