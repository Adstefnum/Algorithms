from typing import Any

#O(log(n) time | O(1) space
def binary_search(array:list,target:Any)->Any:
    
    array.sort()
    left,right=0,len(array)-1
    
    while left <= right:
        mid = (left+right)//2
        
        if array[mid]==target:
            return mid
        
        elif array[mid]<target:
            left = mid + 1
            
        elif array[mid]> target:
            right = mid - 1
            
    return None
    
print(binary_search([1,2,4,5,2.6,7.3,8,3,7,],11))
print(binary_search([1,2,4,5,2.6,7.3,8,3,7,],2.6))
