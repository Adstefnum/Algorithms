#O(n^2) time | O(1) space
def insertionSort(array):

	for i in range(1,len(array)):
		j = i

		while j > 0 and array[j] < array[j-1]:
			swap(j,j-1,array)
			j -= 1
	return array

def swap(i,j,array):
	array[i],array[j] = array[j],array[i]

#O(n^2) time | O(1) space
def insertion_sort(array:list)->list:
    for i in range(1,len(array)):
        key = array[i]
        
        j = i-1
        while j>=0 and array[j]>key:
            arr[j+1]=arr[j]
            j -= 1
        array[j+1]=key
        
    return array
    
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
