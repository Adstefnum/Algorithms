#O(n) space from two O(n) stored dicts
#O(n) time from two O(n) traversing both strings and then dicts have O(1) 
#lookup times
def are_anagrams_1(s1,s2):
  if len(s1)!= len(s2):
    return False
    
  return {i:s1.count(i) for i in s1} == {i:s2.count(i) for i in s2}

#O(n) time from 2 O(n) traversing of both strings 
#O(n) space as Counter returns a dict
def are_anagrams_2(s1,s2):
  if len(s1)!= len(s2):
    return False
    
  from collections import Counter
  return Counter(s1) == Counter(s2)

#They are lexicographically the same text
#O(nlog(n)) time as the sorting algorithm takes O(nlog(n))
#O(1) space as nothing is stored since we sort the string in itself
def are_anagrams_3(s1,s2):
  if len(s1)!= len(s2):
    return False
    
  return sorted(s1) == sorted(s2) 

print(are_anagrams_1('salesman','aelsmsan'))
print(are_anagrams_2('salesman','aelsmsan'))
print(are_anagrams_3('salesman','aelsmsan'))
