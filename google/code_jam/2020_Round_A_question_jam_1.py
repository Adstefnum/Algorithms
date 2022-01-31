
def natural_latin(matrix,n):
    
    #the trace
    a,s=0,0
    trace = 0
    while a < n-1:
        if s <= n-1:
            trace += matrix[a][s]
            a += 1
            s += 1
   
    
     
     #the rows
     j,k=0,0
     row_count,f_row = 0,0
     while k < len(matrix)-1:
         while j < len(matrix[k])-1:
             if matrix[k][j] == matrix[k][j+1]:
                 row_count += 1
                 j += 1
            j += 1
        if row_count:
            f_row += 1
        j = 0
        k += 1
        
        
    #the columns
    l,b = 0,0
    col_count,f_col = 0,0
    while l < n-1:
        while b < len(matrix[l])-1:
            if matrix[b][l] == matrix[b+1][l]:
                col_count += 1
                b += 1
            b += 1
            
        if col_count:
            f_col += 1
        b = 0
        l += 1
        
    return '{} {} {}'.format(trace,f_col,f_row)
        
  

t = int(input())
c = 1

while t >0:
    n = int(input())
    mat = []
    for i in range(n):
        m = list(map(int,input().split()))
        mat.append(m)
    print('Case #{}: {}'.format(c,natural_latin(mat,n)))
    c +=1
    t -= 1