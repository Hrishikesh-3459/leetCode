class Solution:
    def minCostToMoveChips(self, position):
        di = [0, 0]
        for i in position:
            if i & 1 == 1:
                di[0] += 1
            else:
                di[1] += 1
        if di[0] == 0 or di[1] == 0:
            return 0
        return min(di[0], di[1])
