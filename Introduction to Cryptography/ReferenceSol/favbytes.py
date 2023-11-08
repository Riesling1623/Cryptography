input_str = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# We have the format of the flag is crypto{...} so the first letter in the flag is 'c'
# We have ord('c') = 0 ^ ord('c') = input_str[0] ^ input_str[0] ^ ord('c')
# He set the `key` equals to `input_str[0] ^ ord('c')`
# After that, he run through the input string, xor each letters in input_str with key (as above, the first letter is always 'c')

key = input_str[0] ^ ord('c')
print(''.join(chr(c ^ key) for c in input_str))