from superlib import score,xor

def breakSingleByteXor(s):
	l = [xor(s,chr(i)*len(s)) for i in range(256)]
	scores = [score(l[i]) for i in range(256)]
	return l[scores.index(max(scores))]

f = open("4.txt","r")
l = []
for s in f:
	s = s[:-1].decode('hex')
	l.append(breakSingleByteXor(s))

scores = [score(l[i]) for i in range(len(l))]
print l[scores.index(max(scores))]