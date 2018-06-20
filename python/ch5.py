#!/usr/bin/env python
import math

text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

def bxor(b1, b2):
    result = bytearray(b1)
    for i, b in enumerate(b2):
        result[i] ^= b
    return result

def xor_repeat_key(input, key):
    keylen = math.ceil(len(text) / len(key))
    keyarray = bytearray(key * keylen, 'ascii')[0:len(input)]

    result = bxor(bytearray(input, 'ascii'), keyarray)
    return result

print(xor_repeat_key(text, key).hex())
