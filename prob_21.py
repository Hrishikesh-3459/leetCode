# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1 != None:
            while l1:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
        if l2 != None:
            while l2:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
        return cur.next
