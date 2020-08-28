def caesarCipher(string, key):
	output = []
	for s in string:
		newLetCode = ord(s) + key

		if newLetCode > 122:
			newLetCode = 96 + (newLetCode%122)
			output.append(chr(newLetCode))

		else:
			output.append(chr(newLetCode))
	return "".join(output)

print(caesarCipher("xyz",2))
