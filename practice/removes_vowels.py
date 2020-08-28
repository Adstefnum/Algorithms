#receives a string
string = input("Enter a text:")
def disemvowel(string):
	vowels = ['a','e','i','o','u','A','E','I','O','U']

	for s in string:
		if s in vowels:
			out  = string.replace(s,"")
			string = out

	return out
