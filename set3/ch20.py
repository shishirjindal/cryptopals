import os
from superlib import score,xor
from Crypto.Cipher import *

nonce = "\x00"*8
key = os.urandom(16)
data = open("20.txt","r").read()[:-1].split('\n')

def breakSingleByteXor(s):
	l = [xor(s,chr(i)*len(s)) for i in range(256)]
	scores = [score(l[i]) for i in range(256)]
	return chr(scores.index(max(scores)))

def AES_ECB_encrypt(key, data):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(data)

def Generate_Keystream(length, key, nonce):
	keystream = ""
	for i in range(length/16+1):
		data = nonce + chr(i) + "\x00"*(8-len(chr(i)))
		keystream += AES_ECB_encrypt(key, data)
	return keystream

def AES_CTR(keystream, plaintext):
	return xor(keystream, plaintext)

keystream = Generate_Keystream(max([len(i) for i in data]), key, nonce)
ciphertext = []

for plain in data:
	ciphertext.append(AES_CTR(keystream, plain.decode("base64")))

keysize = min([len(i) for i in ciphertext])
ciphertext = [i[:keysize] for i in ciphertext]
blocks = []
for i in range(keysize):
	blocks.append(''.join([j[i] for j in ciphertext]))

for j in ciphertext:
	print xor((''.join([breakSingleByteXor(i) for i in blocks])),j)