__author__ = 'samgu'
import hashlib

def valid_wx(token, timestamp, nonce, signature):
    valid_str = ''.join(sorted([token, timestamp, nonce]))
    valid_str = hashlib.sha1(valid_str).hexdigest()
    if valid_str.lower() == signature.lower():
        return 1
    else:
        return 0