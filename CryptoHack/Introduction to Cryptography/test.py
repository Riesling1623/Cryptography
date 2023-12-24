from pwn import xor

input_str = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(input_str)
print(xor(input_str[7], 'y'.encode()))