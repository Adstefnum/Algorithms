def productSums(array,multiplier = 1):
	Sum = 0

	for element in array:
		if type(element) == list:
			Sum += productSums(element, multiplier+1)

		else:
			Sum += element

	return Sum * multiplier

print(productSums([5,2,[7,-1],3,[6,[-13,8],4]]))