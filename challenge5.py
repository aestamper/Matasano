from challenge2 import fixedXOR

def repeat_to_length(s, length):
   return (s * ((length/len(s))+1))[:length]

def repeatingKeyXOR(s, key):
    key = repeat_to_length(key, len(text))
    return fixedXOR(text, key)

if __name__ == '__main__':
    key = "ICE"
    text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    encrypted_text = repeatingKeyXOR(text, key)
    if encrypted_text.encode("hex") == expected:
        print("Encrypted correctly!")
    else:
        print("Not encrypted correctly.")
