import os
import random
from Crypto.Cipher import *

key = os.urandom(16)
IV = os.urandom(16)

l = ["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
"MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
"MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
"MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
"MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
"MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
"MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
"MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
"MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
"MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]

def pkcs7(plaintext):
	number = 16-len(plaintext)%16
	paddedtext = plaintext+chr(number)*number
	return paddedtext

def xor(s1,s2):
    s3 = "".join([chr(ord(i)^ord(j)) for i,j in zip(s1,s2)])
    return s3

def check_padding(plaintext):
	if ord(plaintext[-1])*plaintext[-1] == plaintext[-ord(plaintext[-1]):]:
		return True,plaintext[:-ord(plaintext[-1])]
	return False,"No"

def AES_CBC_encrypt(plaintext):
	aes = AES.new(key, AES.MODE_CBC, IV)
	return aes.encrypt(plaintext)

def AES_CBC_decrypt(ciphertext):
	aes = AES.new(key, AES.MODE_CBC, IV)
	return aes.decrypt(ciphertext)

def function1(plaintext):
	plaintext = pkcs7(plaintext)
	ciphertext = AES_CBC_encrypt(plaintext)
	return ciphertext

def function2(ciphertext):
	plaintext = AES_CBC_decrypt(ciphertext)
	if check_padding(plaintext)[0] == True:
		return True
	return False

plaintext = random.choice(l)
ciphertext = function1(plaintext)

ciphertext = [ciphertext[i:i+16] for i in range(0,len(ciphertext),16)]
new = ciphertext[:]
plaintext = ""
for k in range(2,len(ciphertext)+1):
	intermediate = ""
	for j in range(1,17):
		var = ciphertext[-k][-j]
		for i in range(256):
			new[-k] = ciphertext[-k][:-j]+chr(i)+xor(intermediate,chr(j)*j)
			if function2(''.join(new[-k]+new[-k+1])):
				intermediate = chr(i^j) + intermediate
				plaintext = chr(i^j^ord(var)) + plaintext
				break
			new = ciphertext[:]
		print plaintext

# now for IV
new = IV[:]
intermediate = ""
for j in range(1,17):
	var = IV[-j]
	for i in range(256):
		new = IV[:-j]+chr(i)+xor(intermediate,chr(j)*j)
		if function2(''.join(new+ciphertext[0])):
			intermediate = chr(i^j) + intermediate
			plaintext = chr(i^j^ord(var)) + plaintext
			break
		new = IV[:]
	print plaintext