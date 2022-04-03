def partition(arr, left, right, pivot):

    while left <=right:

        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
    return left

#Average:O(nlog(n)) time, Worst: O(n^2) time in case of choosing a bad pivot e.g the lowest element
#Average: O(log(n), Worst:O(n) space
def quicksort(arr, left,right):
    
    if len(arr)  == 1:
        return arr

    if left < right:

        pivot_index = (left+right)//2
        pivot = arr[pivot_index]
        idx = partition(arr,left,right,pivot)
        quicksort(arr,left,idx-1)
        quicksort(arr,idx,right)



arr = [2,56,2,8,4,9,5,74,8,35,64,6,3,65,745]
left,right = 0, len(arr)-1
quicksort(arr,left,right)
print(arr)


