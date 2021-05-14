import timeit

#O(n) time | O(1) space
def version1(sequence=[], subSequence=[]):
	seqId = 0
	subSeqId = 0

	while seqId != len(sequence) and subSeqId != len(subSequence):
		if sequence[seqId] == subSequence[subSeqId]:
			subSeqId += 1
		seqId += 1
	return subSeqId == len(subSequence)

#O(n) time | O(1) space
def version2(sequence=[], subSequence=[]):
	subSeqId = 0

	for seq in sequence:
		if subSeqId < len(subSequence):
			if seq == subSequence[subSeqId]:
				subSeqId += 1
	return subSeqId == len(subSequence)
		
#Testing
print(version1([1,2,3,4,5,6],[3,5,6]),timeit.timeit(str(version1([1,2,3,4,5,6],[3,5,6]))))
print(version1([1,2,3,4,5,6],[3,6,5]))
print(version2([1,2,3,4,5,6],[3,5,6]),timeit.timeit(str(version2([1,2,3,4,5,6],[3,5,6]))))
print(version2([1,2,3,4,5,6],[3,6,5]))