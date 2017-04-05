import os
from Crypto.Cipher import AES

key = os.urandom(16)
IV = key

def pkcs7(plaintext):
	number = 16-len(plaintext)%16
	paddedtext = plaintext+chr(number)*number
	return paddedtext

def unpad(plaintext):
	return plaintext[:-ord(plaintext[-1])]

def AES_CBC_encrypt(plaintext):
	aes = AES.new(key, AES.MODE_CBC, IV)
	return aes.encrypt(plaintext)

def AES_CBC_decrypt(ciphertext):
	aes = AES.new(key, AES.MODE_CBC, IV)
	plaintext = aes.decrypt(ciphertext)
	if reduce(lambda x,y : x^y, [True if ord(i) < 128 else False for i in plaintext]):
		print "No error, Run again."
	else:
		raise ValueError(plaintext)

def function1(plaintext):
	plaintext = plaintext.replace(';','').replace('=','')
	plaintext = pkcs7(plaintext)
	ciphertext = AES_CBC_encrypt(plaintext)
	return ciphertext

plaintext = "\x00"*48
ciphertext = function1(plaintext)
try:
	plaintext = AES_CBC_decrypt('\x00'*16+ciphertext[:-16])
except ValueError as plaintext:
	if plaintext.message[16:32] == key:
		print "Yay, Key Cracked!!"
	else:
		"Attack Failed"