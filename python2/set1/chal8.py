#!/usr/bin/env python
from collections import defaultdict

ECB_ciphertext = ''
maxreps = 0

def count_reps(text, block_length=16):
    repeats = defaultdict(lambda: -1)
    for i in range(0, len(text), block_length):
        repeats[text[i:i+block_length]] += 1

    for k,v in repeats.iteritems():
        if v>0:
            print "{} was repeated {} times".format(k,v+1)

    return sum(repeats.values())

for line in list(open("8.txt", "r")):
    ciphertext = line.rstrip()
    
    repeats = count_reps(ciphertext, 16)
    if repeats > maxreps:
        ECB_ciphertext = ciphertext
        maxreps = repeats

print ECB_ciphertext
