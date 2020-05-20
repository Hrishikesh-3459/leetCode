# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        le = 0
        cur = head
        while True:
            if (cur.next == None):
                le += 1
                break
            le += 1
            cur = cur.next
        pos = le // 2
        cur = head
        while True:
            if (pos == 0):
                return cur
            pos -= 1
            cur = cur.next
            
        
