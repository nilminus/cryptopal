#!/usr/bin/env python3
from binascii import unhexlify, hexlify

expected = b'746865206b696420646f6e277420706c6179'

def bxor (a, b):
    return bytes([x^y for (x,y) in zip(a,b)])

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

result = bxor (unhexlify(a), unhexlify(b))
#print (hexlify (result))
#print (result)

if expected == hexlify(result):
    print("[+] CORRECT !")
else:
    print(":(")
