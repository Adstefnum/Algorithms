#O(n^2) in the worst case: if it is reverse sorted
#O(1) space
def bubble_sort(array:list)->list:
    n = len(array)
    
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

#O(n*n) in the worst case: if it is reverse sorted
#O(n) in the best case if it is already sorted
#O(1) space
#The swapped check helps us to stop the swapping loop from running again 
#when the array is already sorted and this saves us some time.
def bubble_sort_2(array:list)->list:
    n,swapped = len(array),False
    
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
        if swapped == False:
            return array
    return array
                
arr = [64, 34, 25, 12, 22, 11, 90]
 
print(bubble_sort(arr))
print(bubble_sort_2(arr))
