# Title: Collatz conjecture program
# Features: Show peak, show number of hail stones, verbose and non-verbose mode(showing of each step)
# Graph with matplotlib
# Author: Stephen Adesina

import numpy as np
import matplotlib.pyplot as plt


x = int(input("Give me a number:"))
count = 0
peak = 0 
x_list = []
y_list = []

while x != 1:
	if x%2==0:
		x /= 2
	else:
		x = 3*x + 1
	count += 1

	if x> peak:
		peak = x
	x_ = x_list.append(x)
	y_ = y_list.append(count) 

plt.plot(np.array(x_),np.array(y_))
plt.title("Collatz Conjecture")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
print(int(peak),count)
