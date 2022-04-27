#num1 num2
#numbers in strings
#"11" "22" = "33"
#don't convert to int and dont support decimal and negatives

def string_add_2(num1:str, num2:str)->str:
    ret = []
    a,b = len(num1)-1,len(num2)-1
    if len(num1)>=len(num2):
        n = len(num1)
    elif len(num1)<len(num2):
        n = len(num2)
        
    for i in range(n):
        sum_ = str(eval(f"{num1[a-i]} + {num2[b-i]}"))
        if int(sum_) > 9:
            rem = str(eval(f"{sum_}-10"))
            if "#1" in ret:
                cr_idx = ret.index("#1")
                ret[cr_idx] = str(eval(f"{rem}+1"))
            else:
                ret.append(rem)
                ret.append("#1")
                
        else:
            if "#1" in ret:
                cr_idx = ret.index("#1")
                ret[cr_idx] = str(eval(f"{sum_}+1"))
            else:
                ret.append(sum_)
            print(ret)
            
    return "".join(ret[::-1])

  #edgecases
  # 1 + 99
  # 1009 +1009
  # 2019 + 2019
print(string_add_2("1","99"))


#num1 num2
#numbers in strings
#"11" "22" = "33"
#don't convert to int and dont support decimal and negatives

def string_add_2(num1:str, num2:str)->str:
    
    #make num 2 the bigger number
    if len(num1)>len(num2):
        temp = num1
        num1 = num2
        num2 = temp
        
    ret = ""
    a,b = len(num1)-1,len(num2)-1
    diff = abs(a-b)
    carry = 0
    
    #loop using the length of the lower number 
    #diff enables us to reach the end of the larger string
    for i in range(a,-1,-1):
        sum_ = str(eval(f"{num1[i]} + {num2[i+diff]} + {carry}"))
        ret += str(eval(f"{sum_}%10"))
        carry = str(eval(f"{sum_}//10"))
    
    for j in range(diff,-1,-1):
        sum_ = str(eval(f"{num2[j]} + {carry}"))
        ret += str(eval(f"{sum_}%10"))
        carry = str(eval(f"{sum_}//10"))

    if carry:
        to_add = str(eval(f"{carry}+{ret[-1]}"))
        print(to_add)
        ret = ret[:-1] + to_add
            
            
    return ret[::-1]

  #edgecases
  # 1 + 99
  # 1009 +1009
  # 2019 + 2019
print(string_add_2("1","99"))
