from __future__ import print_function
from challenge3 import bestXORGuess

def bestScore(items, score_function): # calculates the best guess
    leader = None
    leader_score = 0
    for item in items:
        rval = score_function(item)
        if isinstance(rval, tuple):
            score, others = rval[0], rval[1:]
            others = (item,) + others
        else:
            score = rval
            others = (item,)
        if score > leader_score:
            leader = others
            leader_score = score
    return leader

def unhexlify_file(fobj): # decodes a file of hex encoded lines
    return (line.strip().decode("hex") for line in fobj if line)

if __name__ == '__main__':
    with open ("4.txt", "rb") as f:
        best_guess = bestScore(unhexlify_file(f), bestXORGuess)
        input_string, outcome, byte = best_guess

        print("String {} decoded into {}, using char {}".format(
            input_string.decode('ascii'), outcome.decode('ascii'), chr(byte)
        ))
