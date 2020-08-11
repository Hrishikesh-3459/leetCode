# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root):
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.left and not node.right:
                    ans.append(node.left.val)
                elif node.right and not node.left:
                    ans.append(node.right.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans