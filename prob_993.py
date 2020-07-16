import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isCousins(root, x, y):
    q = [root]
    ans = {}
    while q:
        node = q.pop(0)
        if node:
            tmp = []
            if node.left:
                tmp.append(node.left.val)
            else:
                tmp.append('x')
            if node.right:
                tmp.append(node.right.val) 
            else:
                tmp.append('x')
            ans[node.val] = tmp
            q.append(node.left)
            q.append(node.right)
            
    q = [root]
    levels = []
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
            levels.append(temp)
            tmp.clear()
    # print(ans)
    # print(levels)
    flag = False
    for i in levels:
        if x in i and y in i:
            flag = True
            break
    if flag == False:
        return False
    if flag == True:
        for i in ans:
            if x in ans[i] and y in ans[i]:
                return False
    return True
            