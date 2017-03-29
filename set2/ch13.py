import os
from Crypto.Cipher import *

key = os.urandom(16)

def pkcs7(plaintext):
	number = 16-len(plaintext)%16
	paddedtext = plaintext+chr(number)*number
	return paddedtext

def unpad(plaintext):
	return plaintext[:-ord(plaintext[-1])]

def AES_ECB_encrypt(plaintext):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.encrypt(plaintext)

def AES_ECB_decrypt(ciphertext):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.decrypt(ciphertext)

def parsing_routine(s):
	l = s.split('&')
	dic = {}
	for i in l:
		if '=' in i :
			u,v = i.split('=')
			dic[u] = v
	return dic

def profile_for(email):
	email = 'email='+email.replace('&','').replace('=','')
	uid = 10
	plaintext = email + '&uid=' + str(uid) + "&role=user"
	return AES_ECB_encrypt(pkcs7(plaintext))

def decrypt(ciphertext):
	plaintext = unpad(AES_ECB_decrypt(ciphertext))
	print plaintext
	plaintext = parsing_routine(plaintext)
	if 'role' in plaintext:
		if plaintext['role'] == 'admin':
			print "Welcome Admin!!"
		else:
			print "Welcome User"
	else:
		print "No role"

p1 = 'a'*10 + 'admin' + '\x0b'*11
p2 = 'a'*13
ciphertext1 = profile_for(p1)
ciphertext2 = profile_for(p2)
ciphertext = ciphertext2[:32] + ciphertext1[16:32]
decrypt(ciphertext)
