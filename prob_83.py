# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (head == None):
            return
        l = set()
        currentNode = head
        while True:
            l.add(currentNode.val)
            if (currentNode.next == None):
                break
            else:
                currentNode = currentNode.next
        l1 = sorted(list(l))
        linkedlist = LinkedList()
        for i in l1:
            node = ListNode(i)
            linkedlist.insert(node)
        return(linkedlist.head)
            
            
            
            
            
            
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head 
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
        
            
        
        