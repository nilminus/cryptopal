#!/usr/bin/env python
import string
import binascii

def prepare_characters_frequency():
    # http://www.data-compression.com/english.html
    first_order_stats = '0.0651738 0.0124248 0.0217339 0.0349835 0.1041442 0.0197881 0.0158610 0.0492888 0.0558094 0.0009033 0.0050529 0.0331490 0.0202124 0.0564513 0.0596302 0.0137645 0.0008606 0.0497563 0.0515760 0.0729357 0.0225134 0.0082903 0.0171272 0.0013692 0.0145984 0.0007836 0.1918182'

    floats = [float(i) for i in first_order_stats.split()]
    lower_chars = list(string.ascii_lowercase)
    lower_chars.append(' ')

    return dict(zip(lower_chars, floats))

def english_score(input_bytes):
    score = 0
    for byte in input_bytes:
        letter_frequency = FREQS_CHARACTERS.get(chr(byte).lower())
        if letter_frequency:
            score += letter_frequency
    return score

def single_byte_xor(input_bytes, key):
    output = b''
    return bytes ([char ^ key for char in input_bytes])

def break_single_byte_xor(input_bytes):
    result = {
            'plaintext' : b'',
            'score' : 0,
            'key' : b''
            }
    
    for key in range(256):
        plaintext_candidate = single_byte_xor(input_bytes, key)
        candidate_score = english_score (plaintext_candidate)
        if candidate_score > result['score']:
            result['plaintext'] = plaintext_candidate
            result['score'] = candidate_score
            result['key'] = key

    return result


if __name__ == '__main__':
    encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    FREQS_CHARACTERS = prepare_characters_frequency()
    s = binascii.unhexlify(encoded)
    result = break_single_byte_xor(s)
    for key, value in result.items():
        print(key, value)
