import hashlib
import os

from ..Func.some_func import bxor
from time import sleep
from binascii import hexlify, unhexlify
from urllib.parse import urlparse, parse_qs

def sha1(data):
    '''single-call SHA-1
    (instead of having several calls then a finalization call)'''
    h = hashlib.sha1()
    h.update(data)
    return h.digest()

def hmac_sha1(data, key):
    # see https://datatracker.ietf.org/doc/html/rfc2104
    IPAD = b'\x36'*64
    OPAD = b'\x5C'*64

    return sha1(
        bxor(key, OPAD)
        + sha1(
            bxor(key, IPAD)
            + data
        )
    )

# Testing our implementation against a value I got using the "cryptography" library
assert (
    hmac_sha1(b'test message', b'test key')
    == b'\xbb?\x1a\xdc\x11~\xa0\xed\x15\x9d\x8ek\xaa\xfb\x9d\xff\xe4\x8caZ'
)

class Website:
    def __init__(self):
        self.mac_key = os.urandom(16)

    def handle_query(self, url):
        parsed_query = parse_qs(urlparse(url).query)

        # note the "[0]": function `parse_qs` maps keys to *lists* of values
        # because the HTTP protocol allows the same key to appear several time
        # in a query string
        file = parsed_query['file'][0]
        signature = parsed_query['signature'][0]

        sig_bytes = unhexlify(signature)

        verify_signature(sig_bytes, file.encode(), self.mac_key)

class InvalidSignatureError(Exception):
    pass

def verify_signature(signature, data, key):
    expected_signature = hmac_sha1(data, key)

    for (sig_byte, expected_byte) in zip(signature, expected_signature):
        if sig_byte != expected_byte:
            # this is the "early exit":
            # technically we can reject the signature
            # *as soon as* we found one byte that differs.
            # This however is what will cause the vulnerability
            # that is exploited in this challenge.
            raise InvalidSignatureError

        # the "artificial delay" of 50 milliseconds we are asked to add
        sleep(0.05)

    # We don't return anything:
    # if we didn't raise an exception it means the signature was valid

# instanciation
website = Website()

# Some quick tests

correct_signature = bytes.decode(hexlify(
    hmac_sha1(str.encode('foo'), website.mac_key)
))
# should not raise an error
website.handle_query(f"http://localhost:9000/test?file=foo&signature={correct_signature}")
# should raise an error
wrong_signature = correct_signature[:2] + 'fff' + correct_signature[5:]
try:
    website.handle_query(f"http://localhost:9000/test?file=foo&signature={wrong_signature}")
    # unexpected
    raise Exception('Expected an "InvalidSignatureError"')
except InvalidSignatureError:
    # expected
    pass

def measure_verification_time(signature, website):
    start_time = time.perf_counter_ns()
    try:
        website.handle_query(f"http://localhost:9000/test?file=foo&signature={signature}")
        raise Exception('signature was not rejected')
    except InvalidSignatureError:
        pass
    end_time = time.perf_counter_ns()

    duration = end_time - start_time
    # we return duration in milliseconds
    # (time.perf_counter_ns() returns nanoseconds)
    return duration//1_000_000

import time

timings_first_byte = [
    # see https://docs.python.org/3/library/string.html#formatspec
    # for more information on the formating mini-language (the ":02x" thing)
    (
        measure_verification_time(f'{first_byte:02x}' + '0'*(15*2), website),
        f'{first_byte:02x}',
    )
    for first_byte in range(256)
]

print(sorted(timings_first_byte, reverse=True)[:5])
print(correct_signature[:2])

def recover_next_signature_byte(website, already_recovered):
    timings = list()
    for candidate_byte in range(256):
        candidate_signature = (
            already_recovered
            + f'{candidate_byte:02x}'
            + '0'*(16*2 - len(already_recovered) - 2)
        )

        duration = measure_verification_time(candidate_signature, website)

        if timings:
            # mean timing for *other* bytes
            mean = sum(x[0] for x in timings) / len(timings)

            if duration > mean + 30:
                # this one took much longer,
                # (at least 30 milseconds more than average)
                # that's probably the correct byte,
                # so no need to go further
                recovered_byte = candidate_byte
                break

        timings.append((duration, candidate_byte))
    else:
        # in Python, the "else" block of a "for" loop
        # is executed if the for loop was not exited with a "break"
        longuest = sorted(timings, reverse=True)[0]
        recovered_byte = longuest[1]

    return f'{recovered_byte:02x}'

print('EXPECTED SIGNATURE:', correct_signature)

recovered_signature = str()
for _ in range(16):
    next_byte = recover_next_signature_byte(website, recovered_signature)
    recovered_signature += next_byte
    print(next_byte)