import binascii
from superlib import score,hammingDistance,xor

data = open("6.txt","r").read()[:-1].decode('base64')

def normalized_distance(keysize):
	number_of_blocks = len(data)/keysize
	val = 0
	for i in range(number_of_blocks-1):
		s1 = data[i*keysize:(i+1)*keysize]
		s2 = data[(i+1)*keysize:(i+2)*keysize]
		val += hammingDistance(s1,s2)
	return val/(keysize*number_of_blocks)

def breakSingleByteXor(s):
	l = [xor(s,chr(i)*len(s)) for i in range(256)]
	scores = [score(l[i]) for i in range(256)]
	return chr(scores.index(max(scores)))

l = [normalized_distance(i) for i in range(2,40)]
keysize = l.index(min(l))+2

blocks = []
for i in range(keysize):
	blocks.append("".join([data[j] for j in range(i,len(data),keysize)]))
print "".join([breakSingleByteXor(i) for i in blocks])