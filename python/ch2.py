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

hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'
toproduce = '746865206b696420646f6e277420706c6179'

result = hexxor(hex1, hex2)

if result == toproduce:
    print("Success")
else:
    print("Failure")
