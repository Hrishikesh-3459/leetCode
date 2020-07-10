# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head:
        return
    cur = head
    ev_head = ListNode()
    ev = ev_head
    cur = head
    while cur:
        try:
            pointer = cur
            ev.next = cur.next
            pointer.next = cur.next.next
            ev = ev.next
            cur = pointer.next
        except:
            break
    tmp = head
    while True:
        if tmp.next == None:
            tmp.next = ev_head.next
            return head
        tmp = tmp.next

