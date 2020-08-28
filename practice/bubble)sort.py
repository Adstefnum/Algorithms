def bubbleSort(array):

	checker = False
	counter = 0

	while not checker:
		checker = True

		for j in range(len(array)-1-counter):

			if array[j] < array[j-1]:
				array[j],array[j-1] = array[j-1],array[j]
				checker = False
				j =+ 1
				
		counter += 1

	return array

print(bubbleSort([2,3,5,-6,-1,0,7,9,8,4,1,4,-4]))