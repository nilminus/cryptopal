#y/usr/bin/env python

input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def bxor(b1, b2):
    result = bytearray(b1)
    for i, b in enumerate(b2):
        result[i] ^= b
    return result

def hexxor(hex1, hex2):
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)
    result = bxor(b1,b2)
    return result.hex()

def score(s):
    score = 0
    freq = {}

    freq[' '] = 0.22549
    freq['e'] = 0.12702
    freq['t'] = 0.09056
    freq['a'] = 0.08167
    freq['o'] = 0.07507
    freq['i'] = 0.06966
    freq['n'] = 0.06749
    freq['s'] = 0.06327
    freq['h'] = 0.06094
    freq['r'] = 0.05987
    freq['d'] = 0.04253
    freq['l'] = 0.04025
    freq['c'] = 0.02782
    freq['u'] = 0.02758
    freq['m'] = 0.02406
    freq['w'] = 0.02360
    freq['f'] = 0.02228
    freq['g'] = 0.02015
    freq['y'] = 0.01974
    freq['p'] = 0.01929
    freq['b'] = 0.01492
    freq['v'] = 0.00978
    freq['k'] = 0.00772
    freq['j'] = 0.00153
    freq['x'] = 0.00150
    freq['q'] = 0.00095
    freq['z'] = 0.00074 

    for c in s.lower():
        if c in freq:
            score += freq[c]

    return score

def break_single_xor(b1):

    max_score = 0
    result_plaintext = None
    key = None

    for i in range(1,255):
        b2 = [i] * len(b1)
        candidate = bxor(b1, b2)
        try:
            score_candidate = score(candidate.decode('ascii'))
        
            if max_score < score_candidate:
                max_score = score_candidate
                result_plaintext = candidate.decode('ascii')
                key = chr(i)
        except:
            continue

    return key, result_plaintext

max_score = 0
result_plaintext = None
key = None

for line in open("4.txt", "r"):
    line = line.strip()
    b1 = bytearray.fromhex(line)


    for i in range(0,255):
        b2 = [i] * len(b1)
        candidate = bxor(b1, b2)
        try:
            score_candidate = score(candidate.decode('ascii'))
        
            if max_score < score_candidate:
                max_score = score_candidate
                result_plaintext = candidate.decode('ascii')
                key = chr(i)
        except:
            continue

print(key, result_plaintext)
