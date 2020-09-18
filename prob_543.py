# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = float('-inf')
        self.solve(root)
        return self.res - 1

    def solve(self, root):
        if not root:
            return 0

        l = self.solve(root.left)
        r = self.solve(root.right)

        tmp_ans = 1 + max(l, r)
        ans = max(tmp_ans, 1 + l + r)
        self.res = max(self.res, ans)

        return tmp_ans
