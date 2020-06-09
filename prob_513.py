# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        ans = []
        cur_count = 1
        nxt_count = 0
        tmp = []
        while q:
            node = q.pop(0)
            tmp.append(node.val)
            cur_count = 0
            if node.right:
                q.append(node.right)
                nxt_count += 1
            if node.left:
                q.append(node.left)
                nxt_count += 1
            if cur_count == 0:
                cur_count, nxt_count = nxt_count, cur_count
                t = tmp[-1]
                ans.append(t)
                tmp.clear()
        return ans.pop()
