def are_anagrams_1(s1,s2):
  if len(s1)!= len(s2):
    return False
    
  return {i:s1.count(i) for i in s1} == {i:s2.count(i) for i in s2}

def are_anagrams_2(s1,s2):
  if len(s1)!= len(s2):
    return False
    
  from collections import Counter
  return Counter(s1) == Counter(s2)

#They are lexicographically the same text
def are_anagrams_3(s1,s2):
  if len(s1)!= len(s2):
    return False
    
  return sorted(s1) == sorted(s2) 

print(are_anagrams_1('salesman','aelsmsan'))
print(are_anagrams_2('salesman','aelsmsan'))
print(are_anagrams_3('salesman','aelsmsan'))
