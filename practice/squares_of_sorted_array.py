
#O(n) time and space

def sortedSquares(arr:list)->list:
    #since the array is originally sorted, keep increasing
    #the K to get where the positives start in the array
    k,n = 0,len(arr)
    for k in range(n):
        if arr[k] >= 0:
            break
            
    #left pointer at last negative and right pointer at first positive
    #idx is needed for ?
    i,j,idx =k-1,k,0
    #Instantiate a dummy ist
    result = [0]*n
    
    #If the square of a neg is less than that of the pos put it first or do otherwise
    while i>=0 and j <n:
        if arr[i]*arr[i] < arr[j]*arr[j]:
            result[idx] = arr[i]*arr[i]
            print(result)
            i -= 1
        else:
            result[idx] = arr[j]*arr[j]
            j += 1
            print(result)
        idx += 1
    
    #copying other parts of the original array that might have been left out
    while i>=0:
        result[idx] = arr[i]*arr[i]
        i -= 1
        idx += 1
        
    while j<n:
        result[idx] = arr[j]*arr[j]
        j += 1
        idx += 1
        
    return result
    
#O(n) time and space
def sortedSquares2(nums:list)->list:
    n = len(nums)
    left,right= 0,n-1
    idx = n-1
    result = [0]*n

    while idx>=0:
        if abs(nums[left]) >= abs(nums[right]):
            result[idx] = nums[left]*nums[left]
            left += 1
        else:
            result[idx] = nums[right]*nums[right]
            right -= 1
        idx -= 1
    return result

#How is it sorted automatically??
