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
