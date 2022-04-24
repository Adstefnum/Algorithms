#Average:O(nlog(n)) time, Worst: O(n^2) time in case of choosing a bad pivot e.g the lowest element
#Average: O(log(n), Worst:O(n) space
from typing import Any

def quickSort(array:list,left:int,right:int)->list:
    
    def partition(array:list,left:int,right:int,pivot:Any)->int:
        
        while left <= right:
            
            while array[left] < pivot:
                left += 1
                
            while array[right] > pivot:
                right -= 1
                
            if left <= right:
                array[left],array[right]=array[right],array[left]
                right -= 1
                left += 1
                
        return left
        
    if len(array)==1:
        return array
    
    if left < right:
        pivot = array[(left+right)//2]
        idx = partition(array,left,right,pivot)
        quickSort(array,left,idx-1)
        quickSort(array,idx,right)
        
    return array
        
arr = [2,56,2,8,4,9,5,74,8,35,64,6,3,65,745]
left,right = 0, len(arr)-1
print(quickSort(arr,left,right))
      
        
print(arr)


