s = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
xorkey = "ICE"*(24)+"IC"

print "".join(chr(ord(x)^ord(y)) for x,y in zip(s,xorkey)).encode("hex")