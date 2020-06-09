# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        tmp = []
        cur_count = 1
        nxt_count = 0
        while q:
            node = q.pop(0)
            tmp.append(node.val)
            cur_count -= 1
            if node.left:
                q.append(node.left)
                nxt_count += 1
            if node.right:
                q.append(node.right)
                nxt_count += 1
            if cur_count == 0:
                val = max(tmp)
                ans.append(val)
                tmp.clear()
                cur_count, nxt_count = nxt_count, cur_count
        return ans
