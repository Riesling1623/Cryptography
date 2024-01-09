"""
    CryptoPals - Set 2
    Challenge 9: Implement PKCS#7 padding Solution
"""

# Create padding bytes: Make a list and convert to bytes
def pkcs7_padding(byte_plaintext, block_size):
    # Calculate the padding size
    padding_size = block_size - (len(byte_plaintext) % block_size)
    
    # Create padding bytes
    padding_bytes = bytes([padding_size] * padding_size)

    return byte_plaintext + padding_bytes

if __name__ == "__main__":
    plaintext = "YELLOW SUBMARINE"
    byte_plaintext = bytes(plaintext, 'utf-8')
    block_size = 20
    print(pkcs7_padding(byte_plaintext, block_size))

# done