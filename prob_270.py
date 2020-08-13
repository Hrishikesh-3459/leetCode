# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root, target):
        di = {}
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                cur = abs(node.val - target)
                di[node.val] = cur
                stack.append(node.right)
                stack.append(node.left)
        smol = min(di.values())
        for i in di:
            if di[i] == smol:
                return i