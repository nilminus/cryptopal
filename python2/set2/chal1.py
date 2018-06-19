#!/usr/bin/env python
from struct import pack, unpack
from ..utils import *

def pad_pkcs7(buffer, block_size=16):
    remainder = len(buffer) % block_size
    if not remainder:
        # No padding needed
        return buffer

    padding = block_size - remainder
    # strpad = "\\x{:02x}".format(padding)
    strpad = chr(padding)
    padded = buffer + strpad*padding

    return (padded)

buffer = "YELLOW SUBMARINE"
print pad_pkcs7(buffer, 20).encode('string-escape')
print repr(pad_pkcs7(buffer, 20))

