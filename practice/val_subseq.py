#O(n) time | O(1) space
def version_1(array, seq):
    
    i,j = 0,0
    while j < len(seq) and i < len(array) :
    	if array[i] == seq[j]:
    		j +=1
    	i +=1
    return j == len(seq)

    #we don't use len(seq)-1 becuase we want to read the last element
    #we just want the index to be less than the full length of each array.
    #why isn't the time complexity O(n+m) n and m being the length of each array?

#O(n) time | O(1) space
def version_2(array, seq):
	
	j = 0
	for i in array:
		if j < len(seq):
			if i == seq[j]:
				j += 1 

	return j == len(seq)
    		


print(version_2([2,1,4,5,-1,10,7,8,16,12,13], [1,18,10,16]))
