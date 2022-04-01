#O(n) time as we will have to go through whole list in worst case but not fully twice or we would have O(n^2), we traverse to a point and continue from there.
#O(1) space
def first_and_last(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            start=i

            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start,i]
    return [-1,-1]

#use as many edge cases as possible
#O(log(n)) time, O(1)
def first_and_last_binary_search(arr,target):

#- The boundary conditon of the while loop is setup so that the left is never greater than the right as originally this means it would be greater than the length of the loop and then subsequently it would give a mid that isn't within the range currently being considered by the left to right extents. The equality in the condition is so that it can run once more and find if the element that the left and right coincide on is the mid or not, if the equality condition were not there, we would not be able to determine this.
#
#- if the mid = target and the element to the left of mid is less thna target then return mid 
#- if the middle element is less than target then move the left pointer to the right of the middle element
#- if the middle element is greater than the target then move the right pointer to the left of mid
#- return -1 if the target is never found even after the loop is exited
#
#- For find_end statements 2,3,4 are:
#- if the mid = target and the element to the right of mid is greater than target then return mid 
#- if the middle element is greater than target then move the right pointer to the left of the middle element
#- if the middle element is less than the target then move the left pointer to the right of mid

#O(log(n)) time for binary search, O(1)
    def find_start(arr,target):
        if arr[0] ==  target:
            return 0 #if the first element is the target then of course that is the start
        left,right=0,len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid-1]<target:
                return mid
            elif arr[mid] < target:
                left = mid+1
            else: 
                right = mid -1
        return -1

#O(log(n)) time for binary search, O(1)
    def find_end(arr,target):
        if arr[-1]==target:
            return len(arr)-1
        left,right=0,len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid+1]>target:
                return mid
            elif arr[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return -1

    #edge cases to take care if the array has no elements which means its length is zero, if the first element is greater than target and if the last element is less than target which would mean the target is not in the array as the array is sorted.
    if len(arr)==0 or arr[0] > target or arr[-1] < target:
            return [-1,-1]
    start = find_start(arr,target)
    end = find_end(arr,target)
    return [start,end]

arr = [2,4,5,5,5,5,5,7,9,9,9]
print(first_and_last(arr,5))
print(first_and_last_binary_search(arr,5))
