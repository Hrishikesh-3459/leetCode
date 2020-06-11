# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        cur_count = 1
        nxt_count = 0
        q = [root]
        big = float('-inf')
        tmp = []
        ans = 1
        while q:
            node = q.pop(0)
            cur_count -= 1
            tmp.append(node.val)
            if node.left:
                q.append(node.left)
                nxt_count += 1
            if node.right:
                q.append(node.right)
                nxt_count += 1
            if cur_count == 0:
                cur_count, nxt_count = nxt_count, cur_count
                if sum(tmp) > big:
                    big = sum(tmp)
                    ans = level
                level += 1
                tmp.clear()
        return ans
                
                
