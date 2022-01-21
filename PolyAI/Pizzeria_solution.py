#!/usr/bin/python3
import numpy as np
class Grid:
	def __init__(self):
		pass

	def file_input(self):
		file_name = input("Path to the file:")
		with open(file_name,'r') as file:
			lines = file.read().splitlines()
			pizzerias = []
			n,m = map(int, lines[0].split())
			i = 1

			while i!=m+1:
				pizzeria = list(map(int,lines[i].split()))
				pizzerias.append(pizzeria)
				i += 1
		return pizzerias,n

	def paste_input(self):
		pizzerias = []
		n,m = map(int, input().split())
		while m>0:
			pizzeria = list(map(int,input().split()))
			pizzerias.append(pizzeria)
			m -= 1

		return pizzerias,n

	def receive_input(self):
		opt = int(input(
			"please choose:\n" +
			"1. file input\n" +
			"2. paste input\n"
		))
		if opt == 1:
			return self.file_input()

		if opt == 2:
			return self.paste_input()

	def traverse_grid(self):
		pizzerias,n = self.receive_input()
		grid = [[0 for column in range(n)] for row in range(n)]

		for p in pizzerias:
			x,y = p[0]-1,p[1]-1#zero indexing for array
			R = p[2]+1#Because the range function stops short of the last value
			#this should only happen if the value to be changed is not greater than p.index()+1
			#if p.index()+1 !> all vlaues in grid:
			for i in range(1,R):
				if x+i < n: #limit below original postion
					grid[x+i][y] += 1 
				if x-i >= 0: #limit above original postion
					grid[x-i][y] += 1 
				if y+i < n:#limit to the right of original postion
					grid[x][y+i] += 1
				if y-i >= 0:#limit to the left of original postion
					grid[x][y-i] += 1 


			for i in range(1,R):
				for j in range(1,R-i):
					if x-i>0 and y-j>0:
						grid[x-i][y-j] += 1

					if x-i>0 and y+j<n:
						grid[x-i][y+j] += 1

					if x+i<n and y-j>0:
						grid[x+i][y-j] += 1

					if x+i<n and y+j<n:
						grid[x+i][y+j] += 1
				 


		return np.max(grid)



if __name__ == "__main__":
	g = Grid()
	print(g.traverse_grid())