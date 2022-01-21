def integerReplacement(n):
        c,c1 = 0,0
        if n%2 == 0:
            n /= 2
            c+=1
            c1+=1
            return integerReplacement(n)
        else:
            n1 = n
            n -= 1
            c+=1
            return  integerReplacement(n)
            n1 += 1
            c1+=1
            return integerReplacement(n1)
        return min(c,c1)
print(integerReplacement(8))
        