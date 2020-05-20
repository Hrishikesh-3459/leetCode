# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stri = ""
        while True:
            if (head.next == None):
                stri += str(head.val)
                break
            stri += str(head.val)
            head = head.next
        return (int(stri,2))
        
