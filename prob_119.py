import copy
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [[1], [1, 1]]
        if rowIndex == 1:
            return [1, 1]
        if rowIndex == 2:
            return [1,2,1]
        i = 3
        while i != rowIndex+2:
            tmp = [1]
            cur = ans[-1]
            start = 0
            end = 2
            while len(tmp) != i-1:
                val = sum(cur[start:end])
                tmp.append(val)
                start += 1
                end += 1
            tmp.append(1)
            cl = copy.copy(tmp)
            ans.append(cl)
            tmp.clear()
            i += 1
        return ans[rowIndex]
