#time = O(n)| space = O(n)
def three(array:list,target:int)->list:
    i,j=0,len(array)-1
    values = set()
    for i in range(len(array)-1):
        sum_ = array[i]+array[j]
        
        
        needed = target-sum_
            
        if needed!=array[i] and needed!=array[j]:
            if needed in values:
                return [array[i],array[j],needed]
            values.add(array[i])
            values.add(array[j])
            i += 1
            j -= 1
    return []

print(three([2,3,5,7,9,8,4,1,4,-4], 16))    
print(three([20,3,5,7,9,8,4,1,4,-4], 16))
            
