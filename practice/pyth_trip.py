import math
#time = O(n)| space = O(n)
def version2(nums):
	
	i = 0
	j =len(nums)-1
	values = set()
	for x in range(0,len(nums)-1):
		pdt = (nums[i]^2)+(nums[j]^2)
		pdts = math.sqrt(pdt)

		if pdts in values:
			return pdt,nums[i],nums[j]

		else:
			values.add(nums[i])
			values.add(nums[j])
			i += 1
			j -= 1


	return "No pythagorean triples found"

print(version2([2,3,5,7,9,8,12,4,1,4,13]))