# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf1 = []
        leaf2 = []
        
        stack1 = [root1]
        while stack1:
            node = stack1.pop()
            if node:
                if node.left == None and node.right == None:
                    leaf1.append(node.val)
                stack1.append(node.right)
                stack1.append(node.left)
                
        stack2 = [root2]
        while stack2:
            node = stack2.pop()
            if node:
                if node.left == None and node.right == None:
                    leaf2.append(node.val)
                stack2.append(node.right)
                stack2.append(node.left)
                
        return leaf1 == leaf2
