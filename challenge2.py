def fixedXOR(s1, s2): # XORs two equal length strings
    return "".join(chr(ord(i) ^ ord(j)) for i, j in zip(s1, s2))

hex1 = "1c0111001f010100061a024b53535009181c"
str1 = hex1.decode("hex")
hex2 = "686974207468652062756c6c277320657965"
str2 = hex2.decode("hex")
o = fixedXOR(str1, str2).encode("hex")
print(o)
