# Modes of operation starter

from Crypto.Cipher import AES


# KEY = ?
# FLAG = ?

ciphertext = "188bc9522883a992cd99f9b2b8ec84fb150c1abe17e7a8ed04a768ad1d11fc07"
plaintext = "63727970746f7b626c30636b5f633170683372355f3472335f663435375f217d"

@chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}

print(decrypt(ciphertext))