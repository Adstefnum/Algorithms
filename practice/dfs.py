class Node:
	def __init__(self):
		self.name = name
		self.children = []

	def addChild(self,name):

		self.children.append(Node(name))

		#O(v+e) time => v = vertices = nodes, e = edges = lines between nodes | 
		#O(v) space => v items in returned array or v calls to stack
		#on a single branch trees
	def depthFirstSearch(self,array):

		array.append(self.name)

		for child in self.children:
			child.depthFirstSearch(array)
		return array