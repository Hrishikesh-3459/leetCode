"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ans = 0
        q = [root]
        while q:
            ans += 1
            for i in range(len(q)):
                node = q.pop(0)
                if node.children:
                    for child in node.children:
                        q.append(child)
        return ans
