from itertools import imap
import binascii
import base64
from challenge5 import repeatingKeyXOR
from challenge3 import bestXORGuess

def hammingDistance(s1, s2): # calculates the hamming distance
    diffs = 0
    for ch1, ch2 in zip(s1, s2):
        if ch1 != ch2:
            diffs += 1
    return diffs

def strToBin(s): # converts string to binary
    return bin(int(binascii.hexlify(s), 16))

def decode(fobj): # decodes a file of base64 encoded data
    return base64.b64decode((''.join(fobj.readlines())))

def guessKeySize(s, n): # guesses the best size for key length
    keysizes = [0,0,0]
    scores = [9000.0,9000.0,9000.0]
    index = 0
    for i in range(2, 40):
        s1 = s[0:i - 1]
        s2 = (s[i:2*i-1])
        d = hammingDistance(s1, s2)
        score = (d / float(n * i))
        if (score < scores[index]):
            keysizes[index] = i
            scores[index] = score
            index = 0
            if (scores[1] > scores[0]):
                index = 1
            if (scores[2] > scores[index]):
                index = 2
    return keysizes, scores

def formatCipherText(text, keysize): # splits ciphertext into keysize-sized blocks
    return [text[i:i+keysize] for i in range(0, len(text), keysize)]

def findKey(s):
    bestMg = 0.0;
    bestKey = 0;
    for i in range(256):
        _, mg, byte = bestXORGuess(s.encode("hex"));
        if (mg > bestMg):
            bestMg = mg;
            bestKey = i;
    return chr(bestKey);

if __name__ == '__main__':
    with open('6.txt', 'rb') as f:
        encrypted_data = decode(f)
        keysizes, scores = guessKeySize(encrypted_data, 20)
        blocks = formatCipherText(encrypted_data, 2)
        key = ''
        for block in blocks:
            key += findKey(block)
        print("Key: " + str(key));
        print("Plain: " + str(repeatingKeyXOR(encrypted_data), key.encode("hex")));
