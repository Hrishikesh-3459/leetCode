# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if node:
                if node.val % 2 == 0:
                    if node.left:
                        if node.left.left:
                            ans += node.left.left.val
                        if node.left.right:
                            ans += node.left.right.val
                    if node.right:
                        if node.right.right:
                            ans += node.right.right.val
                        if node.right.left:
                            ans += node.right.left.val
                stack.append(node.right)
                stack.append(node.left)
        return ans
                        
