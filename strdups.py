a = "deeedbbcccbdaa"
k = 3
i,count = 0,1
while i+1 < len(a):

	if a[i] == a[i+1]:
		count += 1
		print(a[i] ,a[i+1],count)

		if count == k:
			x = a.replace(a[i]*k,"")

	else:
		count =1

	i += 1

print(x)

