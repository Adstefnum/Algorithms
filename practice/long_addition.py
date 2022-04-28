#num1 num2
#numbers in strings
#"11" "22" = "33"
#don't convert to int and dont support decimal and negatives
#assume that a letter or empty space will not be added

#O(num1+num2) time as we have to loop over the both strings completely
#O(n+x) space as we always have to store the result which is of lenght equal to
#original numbers but may have a x value more than the input lenght after addition
def string_add_2(num1:str, num2:str)->str:
    
    #make num 2 the bigger number instead of checking for lenght
    if len(num1)>len(num2):
        temp = num1
        num1 = num2
        num2 = temp
        
    rex = []
    a,b = len(num1)-1,len(num2)-1
    diff = abs(a-b)
    carry = 0
    
    #loop using the length of the lower number 
    #diff enables us to reach the end of the larger string
    for i in range(a,-1,-1):
        sum_ = str(eval(f"{num1[i]} + {num2[i+diff]} + {carry}"))
        ret = str(eval(f"{sum_}%10"))
        rex.append(ret)
        carry = str(eval(f"{sum_}//10"))
    
    #if the difference between the length is not zero add the other numbers to the list
    if diff!=0:
        for j in range(diff,-1,-1):
            sum_ = str(eval(f"{num2[j]} + {carry}"))
            ret = str(eval(f"{sum_}%10"))
            rex.append(ret)
            carry = str(eval(f"{sum_}//10"))
    
    #if at the end of the addition there is still a carry left then add it to the last element in the list
    if carry:
        rex[-1] = str(eval(f"{rex[-1]} + {carry}"))
        
        
    #join the string and reverse it as we added from the back to the front        
    return "".join(rex)[::-1]

  #edgecases
  # 1 + 99
  # 1009 +1009
  # 2019 + 2019
  # 54221350301866419569709863044208 +94919791112382438694026971412463
print(string_add_2("54221350301866419569709863044208","94919791112382438694026971412463"))
