# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1, l2):
        if (l1 == None and l2 == None):
            return
        elif (l1 == None):
            return(l2)
        elif (l2 == None):
            return(l1)
        currentNode1 = l1
        currentNode2 = l2
        linkedlist = LinkedList()
        while True:
            if (currentNode1.val < currentNode2.val):
                node = ListNode(currentNode1.val)
                linkedlist.insert(node)
                if (currentNode1.next == None):
                    linkedlist.insert(currentNode2)
                    break
                else:
                    currentNode1 = currentNode1.next
            elif (currentNode1.val > currentNode2.val):
                node = ListNode(currentNode2.val)
                linkedlist.insert(node)
                if (currentNode2.next == None):
                    linkedlist.insert(currentNode1)
                    break
                else:
                    currentNode2 = currentNode2.next
            else:
                node = ListNode(currentNode1.val)
                linkedlist.insert(node)
                if (currentNode1.next == None):
                    linkedlist.insert(currentNode2)
                    break
                else:
                    currentNode1 = currentNode1.next
                node = ListNode(currentNode2.val)
                linkedlist.insert(node)
                if (currentNode2.next == None):
                    linkedlist.insert(currentNode1)
                    break
                else:
                    currentNode2 = currentNode2.next
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