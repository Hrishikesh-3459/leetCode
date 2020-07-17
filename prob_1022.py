# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sumRootToLeaf(root):
    stack = [(root, "")]
    ans = 0
    while stack:
        node, path = stack.pop()
        if node.right:
            stack.append((node.right, path + str(node.val)))
        if node.left:
            stack.append((node.left, path + str(node.val)))
        if not node.left and not node.right:
            path += str(node.val)
            ans += int(path, 2)
    return ans