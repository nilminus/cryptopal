def xor(b1, b2):
    """Return a bytearray of the 2 XORed bytearray parameters"""

    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b


def score(s):
    """Return frequency score based on the letter frequencies of the English language."""

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


def break_single_key_xor(b1):
    """Return tuple of the XOR key + the plaintext
    Based on a frequency score derived by the English language.

    Keyword arguments:
    ciphertext -- the ciphertext that XOR was applied to
    """

    max_score = None
    result_plaintext = None
    key = None

    for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(bytearray(b1), b2))
        line_score = score(plaintext)

        if line_score > max_score or not max_score:
            max_score = line_score
            result_plaintext = plaintext
            key = chr(i)
    return key, result_plaintext


def hamming_str(s1, s2):
    """Return the Hamming distance between two strings, cause of map()"""

    diffs = 0
    bin1 = bin(int(s1.encode('hex'), 16))
    bin2 = bin(int(s2.encode('hex'), 16))

    # for bit1, bit2 in zip(bin1, bin2):
    for bit1, bit2 in map(None, bin1, bin2):
        if bit1 != bit2:
            diffs += 1
    return diffs


def hamming_byte(bin1, bin2):
    """XORing bytes with themselves should result in zero. The amount of ones after XOR is the Hamming distance"""

    diffs = 0
    xored = xor(bin1, bin2)
    for byte in xored:
        diffs += bin(byte).count("1")
    return diffs


def keysize_from_ciphertext(ciphertext):
    """Guess the size of the XOR key applied to a cipher text.

    Keyword arguments:
    ciphertext -- the ciphertext that XOR was applied to
    """

    normalised_hammings = []

    for KEYSIZE in range(3, 40):
      s1 = ciphertext[:KEYSIZE]
      s2 = ciphertext[KEYSIZE:KEYSIZE*2]
      s3 = ciphertext[KEYSIZE*2:KEYSIZE*3]
      s4 = ciphertext[KEYSIZE*3:KEYSIZE*4]

      hammings = float(hamming_str(s1, s2) + hamming_str(s2, s3) + hamming_str(s3, s4))
      hammings = hammings / (KEYSIZE * 3)
      normalised_hammings.append((KEYSIZE, hammings))

    sorted_hammings = sorted(normalised_hammings, key= lambda x: x[1])
    return sorted_hammings
