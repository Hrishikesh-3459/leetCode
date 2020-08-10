class Solution:
    def totalFruit(self, tree):
        if len(set(tree)) == 2:
            return len(tree)
        ans = []
        i = 0 
        tmp = []
        j = []
        while i < len(tree):
            if tree[i] not in tmp:
                j.append(i)
            tmp.append(tree[i])
            i += 1
            if len(set(tmp)) == 3:
                ans.append(len(tmp) - 1)
                tmp.clear()
                j.pop()
                i = j[-1] 
        if not ans:
            return len(tree)
        
        if len(set(tmp)) != 3:
            val = len(tmp)
        else:
            val = 0
        return max(max(ans), val)