def validate_pkcs7(paddedtext):
	lastbyte = paddedtext[-1]
	for i in range(1,ord(lastbyte)+1):
		if paddedtext[-i] != lastbyte:
			return "padding error"
	return paddedtext[:-ord(lastbyte)]

print validate_pkcs7(raw_input())
