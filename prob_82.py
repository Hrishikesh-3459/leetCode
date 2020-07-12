# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):
    if not head:
        return head
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    cur = head
    prev = head
    while cur:
        x = arr.count(cur.val)
        if x > 1:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    if arr.count(head.val) > 1:
        return head.next
    return head