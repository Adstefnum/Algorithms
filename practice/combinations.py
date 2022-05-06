#O(kn^k) time or more strictly O(kn!/(n-k)!k!) and O(1) soace
def combine(self, n: int, k: int) -> List[List[int]]:
    res = []
    def backtrack(start,comb):
        if len(comb)==k:
            #we append a copy so that the list object 
            #is not updated in the return list
            res.append(comb.copy())
            return
        for i in range(start,n+1):
            comb.append(i)
            backtrack(i+1,comb)
            comb.pop()
    backtrack(1,[])
    return res
