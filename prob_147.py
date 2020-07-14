# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def insertionSortList(head):
    ans = ListNode(float('-inf'))
    ans_head = insert(ans, float('-inf'))
    pointer = head
    while pointer:
        insert(ans_head, pointer.val)
        pointer = pointer.next
    return ans_head.next.next
    
    
    
def insert(linked, val):
    if not linked:
        linked.next = val
        return linked
    else:
        cur = linked
        prev = linked
        while True:
            if cur.next == None:
                node = ListNode(val)
                if val < cur.val:
                    prev.next = node
                    node.next = cur
                    return linked
                cur.next = node
                return linked
            if cur.val > val:
                node = ListNode(val)
                prev.next = node
                node.next = cur
                return linked
            else:
                prev = cur
                cur = cur.next