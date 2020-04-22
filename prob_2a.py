class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    l1_list = []
    currentNode = l1
    while True:
        l1_list.append(currentNode.val)
        if(currentNode.next == None):
            break
        else:
            currentNode = currentNode.next
    l2_list = []
    currentNode1 = l2
    while True:
        l2_list.append(currentNode1.val)
        if(currentNode1.next == None):
            break
        else:
            currentNode1 = currentNode1.next
    str1 = ""
    str2 = ""
    out = []
    for i in l1_list[::-1]:
        str1 += str (i)
    for j in l2_list[::-1]:
        str2 += str (j)
    sum = int (str1) + int (str2)
    for k in str(sum):
        out.append(k)
    out = out[::-1]
    out_obj = []
    linkedlist = LinkedList()
    for i in out:
        out_obj.append(ListNode(i))
    for i in out_obj:
        linkedlist.insert(i)
    return(linkedlist.head)

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
    
inp_l1 = [1,8]
inp_l2 = [0]
l1_obj = []
l2_obj = []
ll_1 = LinkedList()
ll_2 = LinkedList()
for i in inp_l1:
    l1_obj.append(ListNode(i))
for i in l1_obj:
    ll_1.insert(i)
for j in inp_l2:
    l2_obj.append(ListNode(j))
for j in l2_obj:
    ll_2.insert(j)


# ll.head = ListNode()
    
print(addTwoNumbers(ll_1.head,ll_2.head))