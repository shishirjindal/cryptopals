from superlib import score,xor

def breakSingleByteXor(s):
	l = [xor(s,chr(i)*len(s)) for i in range(256)]
	scores = [score(l[i]) for i in range(256)]
	return l[scores.index(max(scores))]

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
s = s.decode("hex")
print breakSingleByteXor(s)