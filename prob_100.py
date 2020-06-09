# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q != None:
            return False
        if q == None and p != None:
            return False
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 and node2:
                if (node1.val != node2.val): 
                    return False
                if node1.left == None and node2.left != None:
                    return False
                if node1.right == None and node2.right != None:
                    return False
                if node2.left == None and node1.left != None:
                    return False
                if node2.right == None and node1.right != None:
                    return False
                stack1.append(node1.left)
                stack2.append(node2.left)
                stack1.append(node1.right)
                stack2.append(node2.right)
        if stack1 != stack2:
            return False
        return True
