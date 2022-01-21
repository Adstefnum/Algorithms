#!/usr/bin/python3
import string
import random
import sys
from heapq import *

class Graph:
	def __init__(self):
		self.earth = [0.0, 0.0, 0.0]


	def file_input(self):
		file_name = input("Path to the file:")
		with open(file_name,'r') as file:
			lines = file.read().splitlines()
			zearth = list(map(float, lines[0].split()))
			n = int(lines[1])
			stations = []
			i = 2

			while i!=n:
				station = list(map(float, lines[i].split()))
				stations.insert(-1, station)
				i += 1
		return stations,zearth

	def paste_input(self):
		zearth = list(map(float, input().split()))
		n = int(input())
		stations = []

		while n>0:
			station = list(map(float, input().split()))
			stations.append(station)
			n -= 1

		return stations,zearth

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
		

	def euclidean_distance(self, point_1, point_2):
		return float("{0:.2f}".format(((point_2[0]-point_1[0])**2 + (point_2[1]-point_1[1])**2 + (point_2[2]-point_1[2])**2)**0.5))

	def create_sub_graph(self):
		stations,zearth = self.receive_input()
		sub_graph = {}

		sub_graph['earth'] = self.earth
		sub_graph['zearth'] = zearth
		for i in stations:
			y = ''.join(random.choices(string.ascii_uppercase +
									   string.ascii_lowercase + string.digits, k=6))
			sub_graph[y] = i

		return sub_graph

	def create_graph(self):
		graph = {}
		sub_graph = self.create_sub_graph()
		coord_keys = sub_graph.keys()
		for i in coord_keys:
			sub = {}
			for j in coord_keys:
				dist_btwn_nodes = self.euclidean_distance(sub_graph[i], sub_graph[j])
				if dist_btwn_nodes != 0.0:
					sub[j] = dist_btwn_nodes 

			graph[i]=sub
		graph['earth'].pop('zearth')
		graph['zearth'].pop('earth')
		return graph,coord_keys

	def create_node_data(self):
		node_data = {}
		inf = sys.maxsize
		graph,coord_keys = self.create_graph()
		for i in coord_keys:
			node_data[i] = {"cost":inf,"pred":[]}
		return graph,node_data

	def max_dist_btwn_nodes(self, shortest_path, graph):
		dist_btwn_nodes = 0
		length = len(shortest_path)
		for i in range(length-1):
			if i!=length:
				weight = graph[shortest_path[i]][shortest_path[i+1]]
				if weight > dist_btwn_nodes:
					dist_btwn_nodes = weight

		return dist_btwn_nodes

	def djikstra(self):
		graph,node_data = self.create_node_data()
		src = "earth"
		dest = "zearth"
		node_data[src]['cost'] = 0
		visited = []
		temp = src
		for i in range(len(graph)-1):
			if temp not in visited:
				visited.append(temp)
				min_heap = []
				for j in graph[temp]:
					if j not in visited:
						cost = node_data[temp]["cost"] + graph[temp][j]
						if cost< node_data[j]['cost']:
							node_data[j]['cost'] = cost
							node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
						heappush(min_heap,(node_data[j]['cost'],j))
			heapify(min_heap)
			temp = min_heap[0][1]
		shortest_path = node_data[dest]['pred']+ [dest]


		return self.max_dist_btwn_nodes(shortest_path,graph)

# remove the value of zearth from the dict relating to earth. and earth from that 
#relating to zearthOther too?
#check other dictionaries online
if __name__ == "__main__":
	g = Graph()
	print(g.djikstra())
	

