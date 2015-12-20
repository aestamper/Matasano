from challenge2 import fixedXOR
from collections import Counter
import struct
import math

# frequency of usage for each english character
FREQUENCY_TABLE = {
    b'a':  0.08167,
    b'b':  0.01492,
    b'c':  0.02782,
    b'd':  0.04253,
    b'e':  0.1270,
    b'f':  0.02228,
    b'g':  0.02015,
    b'h':  0.06094,
    b'i':  0.06966,
    b'j':  0.00153,
    b'k':  0.00772,
    b'l':  0.04025,
    b'm':  0.02406,
    b'n':  0.06749,
    b'o':  0.07507,
    b'p':  0.01929,
    b'q':  0.00095,
    b'r':  0.05987,
    b's':  0.06327,
    b't':  0.09056,
    b'u':  0.02758,
    b'v':  0.00978,
    b'w':  0.02360,
    b'x':  0.00150,
    b'y':  0.01974,
    b'z':  0.00074,
}

if isinstance(b'a'[0], int): # needed for Python 2
    FREQUENCY_TABLE = {x[0]: y for x, y in FREQUENCY_TABLE.items()}

def score(a): # scores the outputs
    c = Counter(a.lower())
    length = len(a)
    coefficient = sum(
        math.sqrt(FREQUENCY_TABLE.get(char, 0) * y/length)
        for char, y in c.items()
    )
    return coefficient

def strXOR(s, c): # XORs a string by a character
    output = struct.pack("B", c) * len(s)
    return fixedXOR(output, s)

def bestXORGuess(s): # returns the highest scoring result
    results = ((strXOR(s, c), c) for c in range(0, 256))
    emap = [(score(r[0]), r[0], r[1]) for r in results]
    emap.sort(key=lambda x: x[0], reverse=True)
    winner = emap[0]
    return winner

if __name__  == '__main__':
    hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    str = hex.decode("hex")
    _, outcome, byte = bestXORGuess(str)
    print("Decoded string is: {}, using char {}".format(outcome.decode('ascii'), chr(byte)))
