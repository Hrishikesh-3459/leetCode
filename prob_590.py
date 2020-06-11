"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.PO(root, ans)
        return ans
    def PO(self, root, ans):
        if root:
            for child in root.children:
                self.PO(child, ans)
            ans.append(root.val)
            
