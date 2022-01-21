class Solution:
    def clumsy(self, n: int) -> int:
        y = str(n)
        n -= 1
        op_l = ['*','//','+','-']
        j = 0
        for i in range(n):
            if j <= len(op_l)-1:
                y += f'{op_l[j]}'+str(n)
                
            else:
                j = 0
            n -= 1
            j += 1
            
        return y
    
        