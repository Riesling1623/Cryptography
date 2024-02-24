import os
import urllib

from ..Func.some_func import *

# taken from challenge 16 and adapted
class Oracle:
    def __init__(self):
        self.key = os.urandom(16)
        self.nonce = None
        
    def encrypt(self, msg):
        # using urllib to quote characters (a bit overkill)
        quoted_msg = urllib.parse.quote_from_bytes(msg).encode()
        
        full_msg = (
            b"comment1=cooking%20MCs;userdata="
            + quoted_msg
            + b";comment2=%20like%20a%20pound%20of%20bacon"
        )
        
        if self.nonce == None:
            self.nonce = 0
        else:
            self.nonce += 1
        
        ciphertext = transform_aes_128_ctr(full_msg, self.key, self.nonce)
        
        return self.nonce, ciphertext
    
    def decrypt_and_check_admin(self, ctxt, nonce):
        ptxt = transform_aes_128_ctr(ctxt, self.key, nonce)
        
        if b";admin=true;" in ptxt:
            return True
        else:
            return False

oracle = Oracle()

chosen_plaintext = b'X'*(len(';admin=true'))

nonce, ctxt = oracle.encrypt(chosen_plaintext)

to_xor = (b'\x00'*len(b"comment1=cooking%20MCs;userdata=")
         +bxor(b';admin=true', chosen_plaintext))

altered_ctxt = bxor(ctxt, to_xor)

print(transform_aes_128_ctr(altered_ctxt, oracle.key, nonce))
html_test(oracle.decrypt_and_check_admin(altered_ctxt, nonce))