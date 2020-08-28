import timeit

#time = O(n^2)| space = O(1)
def version1(nums,target):
	for n in nums:
		no = target - n

		for n in nums:
			if no in nums:
				return n,no

			else:
				return "No value pair give the target" 


#time = O(n)| space = O(n)
def version2(nums,target):
	#sorting makes it faster
	nums.sort()
	value_dict = {}
	for n in nums:
		no = target - n
		if no in value_dict:
			return n,no

		else:
			value_dict[n] = True

	return "No value pair give the target"
			
#time = O(nlog(n))| space = O(1)
def version3(nums,target):
	#array must first be sorted
	nums.sort()

	left_pointer = 0
	right_pointer = len(nums)-1

	for n in nums:
		pointer_sum = nums[left_pointer] + nums[right_pointer]
		if pointer_sum == target:
			return nums[left_pointer], nums[right_pointer]

		elif pointer_sum> target:
			right_pointer -= 1

		elif pointer_sum< target:
			left_pointer += 1

	return "No value pair give the target"

#how about finding all not just one possible pairs
print(timeit.timeit(str(version1([2,3,5,7,8,9,4,6,1,4,-4], 10))),version1([2,3,5,7,8,9,4,6,1,4,-4], 10))
print(timeit.timeit(str(version2([2,3,5,7,8,9,4,6,1,4,-4], 10))),version2([2,3,5,7,8,9,4,6,1,4,-4], 10))
print(timeit.timeit(str(version3([2,3,5,7,8,9,4,6,1,4,-4], 10))),version3([2,3,5,7,8,9,4,6,1,4,-4], 10))