#time = O(n)| space = O(n)
def version2(nums,target):
	
	i = 0
	j =len(nums)-1
	value_dict = set()
	for x in range(0,len(nums)-1):
		sum2 = nums[i]+nums[j]
		if not sum2 >= target:
			first_sum = target - sum2
		if first_sum != nums[i] and  first_sum != nums[j]:
			if first_sum in value_dict:
				return nums[i],nums[j],first_sum

			else:
				value_dict.add(nums[i])
				value_dict.add(nums[j])
				i += 1
				j -= 1

	return "No value set give the target"

print(version2([2,3,5,7,9,8,4,1,4,-4], 16))