# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs(head): 
    if not head:
        return head
    if head.next == None:
        return head
    cur = head
    ans = ListNode()
    ans_head = ans
    while cur:
        try:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = cur
            ans.next = tmp
            ans = ans.next
            ans = ans.next
            cur = cur.next
        except AttributeError:
            break
    return ans_head.next