def merge_sort(arr:list):
    
    if len(arr) > 1:
        mid = len(arr)//2
        L, R= arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)
    
    
        i=j=k=0
        while i<len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]=L[i]
                i += 1
            else:
                arr[k]=R[j]
                j += 1
            k += 1
    
        while i<len(L):
            arr[k]=L[i]
            i += 1
            k += 1
    
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k += 1

arr = [2,56,2,8,4,9,5,74,8,35,64,6,3,65,745]
merge_sort(arr)
print(arr)

