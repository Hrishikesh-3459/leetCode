# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        self.solve(root)
        return self.ans

    def solve(self, node):
        if node:
            if node.left:
                x = node.left
                if not x.left and not x.right:
                    self.ans += x.val
            self.solve(node.left)
            self.solve(node.right)
