class Node:
    def __init__(self,val=None,prev,next):
        self.val = val
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
