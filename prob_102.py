# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        cur_count = 1
        nxt_count = 0
        tmp = []
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
                temp = copy.copy(tmp)
                ans.append(temp)
                tmp.clear()
        return ans
        
