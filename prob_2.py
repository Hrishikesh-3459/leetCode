class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
# node_1.data -> node2.data -> node_3.data -> none
    def printList(self):
        list_data = []
        str1= ""
        str2 = ""
        out = []
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            list_data.append(currentNode.data)
            currentNode = currentNode.next
        # print(list_data)
        first_term = list_data[0][::-1]
        second_term = list_data[1][::-1]
        for i in first_term:
            str1 += str (i)
        for j in second_term:
            str2 += str (j)
        sum = int (str1) + int (str2)
        # print(sum)
        for k in str(sum):
            out.append(k)
        out = out[::-1]
        print(out)

   




firstNode = Node([2,4,3])
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node([5,6,4])
linkedlist.insert(secondNode)
# thirdNode = Node("Matthew")
# linkedlist.insert(thirdNode)
linkedlist.printList()
