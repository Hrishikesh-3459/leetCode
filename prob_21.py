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
        l1_list = []
        currentNode = l1
        while True:
            l1_list.append(currentNode.val)
            if(currentNode.next == None):
                break
            else:
                currentNode = currentNode.next
        l2_list = []
        currentNode1 = l2
        while True:
            if(currentNode1.val == None):
                break
            l2_list.append(currentNode1.val)
            if(currentNode1.next == None):
                break
            else:
                currentNode1 = currentNode1.next
        final_list = l1_list + l2_list
        final_list.sort()
        out_obj = []
        linkedlist = LinkedList()
        for i in final_list:
            out_obj.append(ListNode(i))
        for i in out_obj:
            linkedlist.insert(i)
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
        
