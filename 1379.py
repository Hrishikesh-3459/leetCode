# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack1 = [original]
        stack2 = [cloned]
        while stack1:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 and node2:
                if node2.val == target.val:
                    return node2
                stack1.append(node1.left)
                stack2.append(node2.left)
                stack1.append(node1.right)
                stack2.append(node2.right)
