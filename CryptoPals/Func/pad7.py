"""
    CryptoPals - Set 2
    Challenge 9: PKCS#7 padding
"""
class PaddingError(Exception):
    pass

def pkcs7(b: bytes, block_size: int = 16) -> bytes:
    if block_size == 16:
        pad_len = block_size - (len(b) & 15)
    else:
        pad_len = block_size - (len(b) % block_size)
    return b + bytes([pad_len] * pad_len)

def strip_pkcs7(b:bytes) -> bytes:
    """
        Use to remove the padding
    """
    n = b[-1]
    if n == 0 or len(b) < n or not b.endswith(bytes([n])*n):
        raise PaddingError
    return b[:-n]

if __name__ == "__main__":
    plaintext = b"YELLOW SUBMARINE"
    padded = pkcs7(plaintext)
    unpadded = strip_pkcs7(padded)

    print(f"{padded = }")
    print(f"{unpadded = }")