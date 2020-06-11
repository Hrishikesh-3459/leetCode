"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import copy
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return 
        q = [root]
        cur_count = 1
        nxt_count = 0
        ans = []
        tmp = []
        while q:
            node = q.pop(0)
            cur_count -= 1
            tmp.append(node.val)
            if node.children:
                for child in node.children:
                    q.append(child)
                    nxt_count += 1
            if cur_count == 0:
                cur_count, nxt_count = nxt_count, cur_count
                t = copy.copy(tmp)
                ans.append(t)
                tmp.clear()
        return ans
