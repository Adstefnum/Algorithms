def bubble_sort(array:list)->list:
    n = len(array)
    
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
                
arr = [64, 34, 25, 12, 22, 11, 90]
 
print(bubble_sort(arr))
