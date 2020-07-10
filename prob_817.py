# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def numComponents(head, G):
    ans = 0
    cur = head
    while cur:
        if cur.val in G:
            while cur:
                if cur.val not in G:
                    break
                cur = cur.next
            ans += 1
        else:
            cur = cur.next
    return ans