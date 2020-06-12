# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return
        slow = head
        fast = head
        for i in range(n-1):
            fast = fast.next
        prev = None
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
        if slow == head:
            return head.next
        prev.next = prev.next.next
        return head
            
