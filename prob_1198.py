class Solution:
    def smallestCommonElement(self, mat):
        first = mat.pop(0)
        for i in first:
            flag = True
            for j in mat:
                if i not in j:
                    flag = False
                    continue
            if flag:
                return i
        return -1