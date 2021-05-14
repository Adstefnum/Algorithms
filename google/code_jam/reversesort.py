def rev_cost(ent):
    
    dup_ent = sorted(ent)
    ind_cost,tot = 0,0
    
    for i in range(len(ent)-1):
        ind_cost = abs(i - dup_ent.index(ent[i]))
        print(i,dup_ent.index(ent[i]),ind_cost)
        tot += ind_cost
        
    return tot


test_cases = int(input())
c = 1

while test_cases > 0:
    n = int(input())
    ent = list(map(int,input().split()))
    
    print('Case #{}: {}'.format(c,rev_cost(ent)))
    c += 1
    test_cases -= 1