import os
import sys
from Crypto.Cipher import *

key = os.urandom(16)
IV = os.urandom(16)
prepend = "comment1=cooking MCs;userdata="
append = ";comment2=like a pound of bacon"

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
	return aes.decrypt(ciphertext)

def function1():
	userinput = sys.argv[1]
	userinput = userinput.replace(';','').replace('=','')
	plaintext = prepend+userinput+append
	plaintext = pkcs7(plaintext)
	ciphertext = AES_CBC_encrypt(plaintext)
	return ciphertext

def function2(ciphertext):
	plaintext = AES_CBC_decrypt(ciphertext)
	plaintext = unpad(plaintext)
	plaintext = plaintext.split(";")
	if "admin=true" in plaintext:
		return True
	else:
		return False


ciphertext = function1()
ciphertext = [ciphertext[i:i+16] for i in range(0,len(ciphertext),16)]

# now i change the ciphertext such that after decrypting it contains admin=true for input of he$admin$true

ciphertext[1] = chr(ord('$')^ord(';')^ord(ciphertext[1][0]))+ciphertext[1][1:6]+chr(ord(ciphertext[1][6])^ord('$')^ord('='))+ciphertext[1][7:]
print function2(''.join(ciphertext))

