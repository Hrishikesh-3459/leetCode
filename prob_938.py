# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = []
        self.dfs(root, ans)
        i = 0
        new = []
        for i in ans:
            if i in range(L, R+1):
                new.append(i)
        return sum(new)
    def dfs(self, root, ans):
        if root:
            self.dfs(root.left, ans)
            ans.append(root.val)
            self.dfs(root.right, ans)
            
        
