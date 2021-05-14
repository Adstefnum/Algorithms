#O(n^2) time | O(1) space
def version_1(array, targetsum):

	for i in array:
		for j in array:
			if i!=j and i+j == targetsum:
				return i,j

	return []


#O(n) time | O(n) space
#sorting can make this one faster
def version_2(array, targetsum):

	nums = {}

	for i in array:
		needed = targetsum-i

		if needed in nums:
			return i, needed

		else:
			#we add the number we have checked not the resulting value
			nums[i] = True

	return []


#O(nlog(n)) time | O(1) space
#What makes up this time complexity:the sorting algorithm and the actual time of running the loop. 
#Is the sorting alg log(n) and the loop n?
def version_3(array, targetsum):

	array.sort()

	left = 0
	right = len(array)-1

	while left < right:
		if array[left] + array[right] == targetsum:
			return array[left], array[right]

		elif array[left] + array[right] > targetsum:
			right -= 1


		elif array[left] + array[right] < targetsum:
			left += 1

	return []


print(version_3([5,6,8,3,-4,-1,11],10))
print(version_2([5,6,8,3,-4,-1,11],10))
print(version_1([5,6,8,3,-4,-1,11],10))
