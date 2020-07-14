# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def partition(head, x):
    smol = ListNode()
    smol_head = smol
    big = ListNode()
    big_head = big
    cur = head
    while cur:
        if cur.val < x:
            smol.next = ListNode(cur.val)
            smol = smol.next
        else:
            big.next = ListNode(cur.val)
            big = big.next
        cur = cur.next
    smol.next = big_head.next
    head = smol_head.next
    return head
    