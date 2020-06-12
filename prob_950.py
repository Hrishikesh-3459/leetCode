class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # le = len(deck)
        # arr = [0] * len(deck)
        # if le == 1:
        #     return deck
        # deck.sort()
        # flag = True
        # i = 0
        # arr[0] = deck.pop(0)
        # while arr.count(0):
        #     if arr[i] == 0 and flag == False:
        #         arr[i] = deck.pop(0)
        #         flag = True
        #     elif arr[i] == 0 and flag == True:
        #             flag = False
        #     i += 1
        #     if i == le:
        #         i = 0
        # return arr
        
        
        
        le = len(deck)
        if le == 1:
            return deck
        deck.sort()
        ll = LinkedList()
        for i in range(len(deck)):
            a = node(0)
            ll.insert(a)
        cur = ll.head
        while True:
            if cur.next == None:
                cur.next = ll.head
                break
            cur = cur.next
        ll.head.val = deck.pop(0) 
        cur = ll.head
        flag = True
        while deck:
            if cur.val == 0 and flag == False:
                cur.val = deck.pop(0)
                flag = True
            elif cur.val == 0 and flag == True:
                    flag = False
            cur = cur.next
        ans = []
        cur = ll.head
        for i in range(le):
            ans.append(cur.val)
            cur = cur.next
            
        return ans
            
            
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head 
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
        
