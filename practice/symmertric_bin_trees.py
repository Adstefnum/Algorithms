def are_symmetric(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.key != root2.key:
        return False
    else:
        #laterally inverted
        return are_symmetric(root1.left,root2.right) and are_symmetric(root1.right, root2.left)

#time : O(n) for dfs
# space: O(log(n)) as it is bounded what about unbounded trees?
def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)


class Node:

    # Utility function to create new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

oot = Node(1)
oot.left = Node(2)
oot.right = Node(3)
oot.left.left = Node(4)
oot.left.right = Node(5)
oot.right.left = Node(6)
oot.right.right = Node(7)
oot.right.left.right = Node(8)

print(is_symmetric(root))
print(is_symmetric(oot))
