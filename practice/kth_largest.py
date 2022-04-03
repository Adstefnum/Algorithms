# time: (k-1)*n for getting the max of arr in the loop + O(n) for returning the final max element = O(kn)
#space: O(n)

def kth_largest_1(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))

    return max(arr)

#O(nlog(n)) time for sorting algorithm
# space depends on sorting algorithm
def kth_largest_sorted(arr,k):
    arr.sort()

    return arr[len(arr)-k]

#time: O(n+klog(n)). This can be better than sorted if k is small or zero bcos the time approaches O(n) but when k and n are close then time is O(nlog(n)) as in sorted
# O(n) space for the priority queue
def kth_largest_heapq(arr,k):
    #python uses min heap but we need max heap so we reverse the order so tha the max positive is the min negative
    # this is a priority queue
    arr = [-e for e in arr]#O(n)

    import heapq
    heapq.heapify(arr)#O(n)

    for i in range(k-1):#O(k-1)*log(n)
        heapq.heappop(arr)

    return -heapq.heappop(arr)#O(log(n)

arr = [1,6,3,7,8,4,8,39,11]
ar = [1,6,3,7,8,4,8,39,11]
a = [1,6,3,7,8,4,8,39,11]
k =4
print(kth_largest_1(arr,k))
print(kth_largest_sorted(ar,k))
print(kth_largest_heapq(a,k))
