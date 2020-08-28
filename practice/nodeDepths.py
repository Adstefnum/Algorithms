#O(n) time | O(h) space
def nodeDepths(root):
	depth = 0
	stack = [{"node":root,"depth":0}]
	
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo['node'],nodeInfo['depth']

		if node is None:
			continue
		depths += depth
		stack.append({"node":node.left,"depth":depth+1})
		stack.append({"node":node.right,"depth":depth+1})
	return depths
	
#O(n) time | O(h) space
def nodeDepths2(root,depth=0):
	if root is None:
		return 0

	return depth = depth + nodeDepths2(root.left,depth+1) + nodeDepths2(root.right,depth+1)