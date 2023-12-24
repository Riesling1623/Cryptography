from pwn import xor

input_str = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# Before, we find the possible key is "myXORke" and when xor in some path of the input string like below (using offset)
# We fing the key length = 8, so the last character in the possible key maybe 'y'
# XOR it and we find '1' in the last like below
fmt_flag = "crypto{1"
key = "".join([chr(input_str[i]^ord(fmt_flag[i])) for i in range(8)])

# Find the key length that makes sense
# xored = xor(input_str[8:(8+7)], key.encode())
xored = xor(input_str, key.encode())
print(xored)