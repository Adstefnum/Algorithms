def max_houses(b,prices):
    
    prices.sort()
    i = 0
    
    while b >= prices[i]:
        b -= prices[i]
        i += 1
        
    return i
  
test_cases = int(input())
case_count = 1
while test_cases > 0:
    
    n,b = map(int,input().split())
    prices = list(map(int, input().split()))
    
    print('Case #{}: {}'.format(case_count, max_houses(b,prices)))
    
    test_cases -= 1
    case_count += 1