# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = [root]
        ans = []
        cur_count = 1
        nxt_count = 0
        stack = []
        while q:
            node = q.pop(0)
            cur_count -= 1
            stack.append(node.val)
            if node.left:
                q.append(node.left)
                nxt_count += 1
            if node.right:
                q.append(node.right)
                nxt_count += 1
            if (cur_count == 0):
                ave = sum(stack) / len(stack)
                ans.append(ave)
                stack.clear()
                cur_count, nxt_count = nxt_count, cur_count
        return ans
