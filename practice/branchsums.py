
#the binary tree
class Tree:
	def __init__(self):
		self.value = value
		self.left = None
		self.right = None

#O(n) time| O(n)space
def branchsums(root):
	sums = []
	branchSumsHelper(root,0,sums)
	return sums

def branchSumsHelper(node,runnungSum,sums):

	#if base node is none, return nothing
	if node is None:
		return 

	runnungSum += node.value

	#checking if we are at a leaf node
	if node.left == None or node.right == None:
		sums.append(sums)
		return 

	'''Using an else here means that if both conditions above are false then and 
	only then run this which means even if the root node is None(Tree is none-exsistent)
	 this will run forever as there will be no end point(leaf node), not 
	 using an else means it runs irrespective but if node.left is None
	when it runs the function the first ciondition will catch it as it is the base node then '''
	branchSumsHelper(node.left,runnungSum,sums)
	branchSumsHelper(node.right,runnungSum,sums)
