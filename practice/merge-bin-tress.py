#O(n) time and O(1) space. dfs
  def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root1 and not root2:
          return None
      elif not root1  and root2:
          return root2
      elif root1 and not root2:
          return root1
      elif root1 and root2:
          root1.val += root2.val
          root1.left = self.mergeTrees(root1.left,root2.left)
          root1.right = self.mergeTrees(root1.right,root2.right)
      return root1
