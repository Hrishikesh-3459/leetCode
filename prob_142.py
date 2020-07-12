# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    seen = []
    cur = head
    while cur:
        if cur in seen:
            return cur
        else:
            seen.append(cur)
        cur = cur.next
    return None