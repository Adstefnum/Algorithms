#find the universal set given an array and some subsets of it
#also detect invalid subsets
#probably take the longest one as the default and the check through for subset matches
#if all subset are found in it, yes, if not no universal set

#O(n) time | O(1) space
def subsetFind(sequence=[], subSequence=[]):
	seqId = 0
	subSeqId = 0

	while seqId != len(sequence) and subSeqId != len(subSequence):
		if sequence[seqId] == subSequence[subSeqId]:
			subSeqId += 1
		seqId += 1
	return subSeqId == len(subSequence)

#O(n) time | O(1) space
def uniSet(array=[[]]):
	sorted_tuple =  sorted(array,key = lambda x: len(x))
	posUniset = sorted_tuple[-1]
	for arr in sorted_tuple[0:-2]:
		posSubset = subsetFind(posUniset,arr)

	if posSubset == True:
		return str(posUniset)+"is the universal set"

	else:
		return "No Universal set present"


print(uniSet([[1,2,3,4,5,6,7,8,9,10],[3,2,4],[1,8,5,6,10],[1,2,3,4,5,6,7,8,9],[1,7,5,6,9]]))