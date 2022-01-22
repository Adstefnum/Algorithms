def max_beauty(n,k,p,b):
    
#get the max value in all sub lists
#compare to find the highest and arrange in asc to set an order of preference
#


t = int(input())
c = 1

while t > 0 :
    n,k,p = map(int, input().split())
    b = [ list(map(int, input().split())) for i in range(n)]
    print('Case #{}: {}'.format(c, max_beauty(n,k,p,b)))
    
    
    t -= 1
    c += 1