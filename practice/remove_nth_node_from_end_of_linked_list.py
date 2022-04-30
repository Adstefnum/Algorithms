
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      if head == None:
          return None

      fast=slow=head
      #take the fast pointer n steps forward
      while n>0:
          fast = fast.next
          n -=1

      #if the node at n steps from head is none return head
      #no need to delete anything as the node to be deleted cannot exist

      if fast is None:
          return head.next
      else:
          #looking one step ahead to see that the node we want to assign to the 
          #fast pointer is not null. We keep doing this until we reach the end
          #THis works because we have already gone n steps forward for the fast pointer
          #which now gives the limit of how far forward we can go i.e x steps where x is 
          #the number of nodes between the current node fast points to and the end of
          #the linked list.
          while fast.next is not None:
              fast = fast.next
              slow = slow.next
          #detach the node after slow from the list
          #by setting the next node to the node slow points to to the next of the next
          slow.next = slow.next.next
      return head
      #How do we take care of the case in which we are given n greater than 
      #the length of the list
