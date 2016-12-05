s = "1c0111001f010100061a024b53535009181c"
xor = "686974207468652062756c6c277320657965"
print "".join([chr(ord(x)^ord(y)) for x,y in zip(s.decode("hex"),xor.decode("hex"))]).encode("hex")