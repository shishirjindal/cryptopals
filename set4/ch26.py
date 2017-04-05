import os
from Crypto.Cipher import AES
from Crypto.Util import Counter

key = os.urandom(16)
start = os.urandom(16)
prepend = "comment1=cooking MCs;userdata="
append = ";comment2= like a pound of bacon"

ctr_e = Counter.new(128, initial_value=long(start.encode("hex"), 16))
ctr_d = Counter.new(128, initial_value=long(start.encode("hex"), 16))

def AES_CTR_encrypt(plaintext):
	aes = AES.new(key, AES.MODE_CTR, counter = ctr_e)
	return aes.encrypt(plaintext)

def AES_CTR_decrypt(ciphertext):
	aes = AES.new(key, AES.MODE_CTR, counter = ctr_d)
	return aes.decrypt(ciphertext)

def function1():
	print "Enter input :", 
	userinput = raw_input()
	userinput = userinput.replace(';','').replace('=','')
	plaintext = prepend+userinput+append
	ciphertext = AES_CTR_encrypt(plaintext)
	return ciphertext

def function2(ciphertext):
	plaintext = AES_CTR_decrypt(ciphertext)
	plaintext = plaintext.split(";")
	if "admin=true" in plaintext:
		print "Welcome Admin!!"
	else:
		print "Get the hell out of here"

ciphertext = function1()
ciphertext = [ciphertext[i:i+16] for i in range(0,len(ciphertext),16)]

# modify ciphertext to inject admin=true. input = he$admin$true

ciphertext[2] = chr(ord('$')^ord(';')^ord(ciphertext[2][0]))+ciphertext[2][1:6]+chr(ord(ciphertext[2][6])^ord('$')^ord('='))+ciphertext[2][7:]
function2(''.join(ciphertext))