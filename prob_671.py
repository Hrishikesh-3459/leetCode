# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        values = set()
        self.solve(root, values)

        min1, ans = root.val, float('inf')
        for v in values:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1

    def solve(self, node, values):
        if node:
            self.solve(node.left, values)
            values.add(node.val)
            self.solve(node.right, values)
