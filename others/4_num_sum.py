#time = O(n)| space = O(n)
def version2(nums,target):
	
	i = 0
	j =len(nums)-1
	k = j//2
	value_dict = set()
	value_dict.add(nums[k])
	for x in range(0,len(nums)-1):
		if nums[i] != nums[j] != nums[k]:
			sum2 = nums[i]+nums[j]+nums[k]
		if not sum2 >= target:
			first_sum = target - sum2
		if first_sum != nums[i] and  first_sum != nums[j] and first_sum != nums[k]:
			if first_sum in value_dict:
				return nums[i],nums[j],nums[k],first_sum

			else:
				value_dict.add(nums[i])
				value_dict.add(nums[j])
				i += 1
				j -= 1
				#k += 1

	return "No value set give the target"

print(version2([2,3,7,9,8,6,4,1,4,-4], 16))