class Tree:
    
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

#O(n) time as addition is a constant time operation carried out on all the nodes visited
#this is dfs so only the stack matters because it is recursive hence the space is O(1+log(n)base2)
#The stack matters because recursion causes all operations to be piled on the stack until the last call is called 
#and then works its way back to the top -LIFO and so all these remain on the stack. The space compplexity simply corresponds
#to the height of the tree and since at each level of the tree, the tree is split into two we have log(n)
# or it could simply be O(h) signifying the height of the tree?
# In breadth first searcha queue is used so that adds to the space complexity gotten from the stack as it is also recursive
def tree_sum(root):
    if root is None:
        return 0
    
    left = tree_sum(root.left)
    right = tree_sum(root.right)
    
    return root.key + left + right
    
if __name__ == '__main__':
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)
    root.right.left.right = Tree(8)
    
    print(tree_sum(root))
