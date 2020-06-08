# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        cur = [root]
        while cur:
            node = cur.pop()
            if node:
                if (node.val != val):
                    return False
                cur.append(node.right)
                cur.append(node.left)
        return True
