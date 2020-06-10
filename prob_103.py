# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return 
        q = [root]
        cur_count = 1
        nxt_count = 0
        ans = []
        tmp = []
        flag = True
        while q:
            node = q.pop(0)
            cur_count -= 1
            tmp.append(node.val)
            if node.left:
                nxt_count += 1
                q.append(node.left)
            if node.right:
                nxt_count += 1
                q.append(node.right)
            if cur_count == 0:
                nxt_count, cur_count = cur_count, nxt_count
                t = copy.copy(tmp)
                if flag == True:
                    ans.append(t)
                    flag = False
                elif flag == False:
                    ans.append(t[::-1])
                    flag = True
                tmp.clear()
        return ans
                
