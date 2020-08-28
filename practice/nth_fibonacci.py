#O(2^n) time | O(n) space
def fib1(n):
	if n == 2:
		return 1

	elif n == 1:
		return 0

	return fib1(n-1) + fib1(n-2)	

#O(n) time | O(n) space
def fib2(n, memoize = {1:0,2:1}):
	if n in memoize:
		return memoize[n]

	else:
		memoize[n] = fib2(n-1,memoize) + fib2(n-2,memoize)
		return memoize[n]

#O(n) time | O(1) space
def fib3(n):
	firstTwo = [0,1]
	counter = 3
	while counter <= n:
		fib = firstTwo[0] + firstTwo[1]
		firstTwo[0] = firstTwo[1]
		firstTwo[1] = fib
		counter += 1
	return firstTwo[1] if n>1 else firstTwo[0]


print(fib2(100))