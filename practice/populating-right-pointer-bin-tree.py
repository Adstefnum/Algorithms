#bfs O(n) time and O(1) space as we shaved off the queue
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
      cur,nxt=root,root.left if root else None

      while cur and nxt:
          cur.left.next = cur.right
          if cur.next:
              cur.right.next = cur.next.left
          cur = cur.next
          if not cur:
              cur = nxt
              nxt = cur.left
