class Solution:
    def numSpecial(self, mat):
        x = []
        ans = 0
        for i, row in enumerate(mat):
            if row.count(1) == 1:
                x.append([i, row.index(1)])
        for i, col in enumerate(zip(*mat)):
            if col.count(1) == 1:
                # Here we are reversing the order cause we have taken transpose
                tmp = [col.index(1), i]
                if tmp in x:
                    ans += 1
        return ans
