#Definiton of linked list node class
class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

#Linked list class       
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self,val):
        newNode = Node(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
            
    def deleteNodeByValue(self,value):
        temp = self.head
        
        if temp is not None:
            if temp.val==value:
                self.head = temp.next
                temp = None
                return
            
        while temp is not None:
            if temp.val==value:
                break
            prev = temp
            temp = temp.next
            
        if temp is None:
            return
                
        prev.next = temp.next
        temp = None
    
    def deleteNodeByIndex(self,index):
        if self.head is None:
            return
        if index==0:
            self.head=self.head.next
            return
        idx_count, prev=current=temp=0,self.head
        while current is not None:
            if idx_count==index:
                temp = current.next
                break
            prev = current
            current = current.next
            idx_count += 1
        prev.next = temp
        #set temp to None?
        #check len of LinkedList to find if position exceeds it
    
    def print_ll(self):
        current,to_print = self.head,""
        while current:
            to_print += str(current.val)+"->"
            current = current.next
        print(to_print,"null")
        
LL = LinkedList()
LL.insertNode(3) 
LL.insertNode(2) 
LL.insertNode(4) 
LL.insertNode(5) 
LL.insertNode(6) 
LL.print_ll()
LL.deleteNodeByValue(4)
LL.deleteNodeByValue(5)
LL.print_ll()
    
