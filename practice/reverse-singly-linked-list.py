
#     #iterative O(n) time and O(1) space
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      cur,prev =head,None

      while cur:
          nxt = cur.next
          cur.next = prev
          prev = cur
          cur = nxt
      return prev



class Solution:
  #recursive O(n) time and O(n) space
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

      if not head:
          return None

      newHead = head
      if head.next:
          newHead = self.reverseList(head.next)
          head.next.next = head
      head.next = None
      return newHead
