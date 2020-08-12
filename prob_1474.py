# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNodes(self, head, m, n):
        ans = ListNode()
        fin = ans
        cur = head
        while cur:
            for i in range(m):
                ans.next = cur
                cur = cur.next
                ans = ans.next
                if not cur:
                    ans.next = None
                    break
            if not cur:
                ans.next = None
                break
            for i in range(n):
                cur = cur.next 
                if not cur:
                    ans.next = None
                    break
        return fin.next