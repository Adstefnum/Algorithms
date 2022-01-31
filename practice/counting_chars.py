
a = "deeedbbcccbdaa"
'''
##For non-consecutive repreated characters

#Algorithm
c= {i:a.count(i) for i in a}
print(c)


#Pre bulit Libraries
from collections import Counter


c2 = Counter(a)
print(c2)
'''





##For consecutive repreated characters

#Algorithm

#count is 1 because the increment of count is based
#on equal chars and if there are none then count remains as zero
i,count = 0,1
collections = []
while i+1 < len(a):

	if a[i] == a[i+1]:
		count += 1

	else:
		collections.append([a[i],count])
		count = 1
	i += 1
collections.append([a[i],count])
print(collections)



count=1
length=[]
if len(a)>1:
    for i in range(1,len(a)):
       if a[i-1]==a[i]:
          count+=1
       else :
           length.append([a[i-1],count])
           count=1
    length.append([a[i],count])
else:
    i=0
    length.append([a[i-1],count])
print (length)

 
'''

#Pre bulit Libraries

from itertools import groupby 

res = [len(list(j)) for _, j in groupby(a)] 
print(res)



import re
 
res2 = [len(sub.group()) for sub in re.finditer(r'(.)\1*', a)] 
print(res2)

'''