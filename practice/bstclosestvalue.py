# n calls to the tree
#O(n) time| O(n) space?? O(nlog())
def bstclose(bst,key):

	if bst == None:
		return bst.root

	#if the new value is lesser meaning it is closer change closest to the new value
	if abs(bst.value - key) < abs(key - closest):
		closest = bst.value

	#if key lesser go to left
	if key < bst.value:
		bstclose(bst.value,key)

	#if key greater go to value
	elif key > bst.value:
		bstclose(bst.value,key)

	else:
		return closest

#sinle call to tree, then call on already called??
#O(n) time| O(1) space?? O(nlog())
def recurbstclose(bst,key):
	#store tree in var so we don't use up much space by calling back to tree
	tree = bst
	
	while tree is not None:
	#if the new value is lesser meaning it is closer change closest to the new value
	if abs(tree.value - key) < abs(key - closest):
		closest = tree.value

	#if key lesser go to left
	if key < tree.value:
		recurbstclose(tree.value,key)

	#if key greater go to value
	elif key > tree.value:
		recurbstclose(tree.value,key)

	else:
		return closest
