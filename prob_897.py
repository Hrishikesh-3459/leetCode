# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorder(root, arr)
        ans = TreeNode()
        head = ans
        while arr:
            ans.right = TreeNode(val=arr.pop(0))
            ans = ans.right
        return head.right

    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
