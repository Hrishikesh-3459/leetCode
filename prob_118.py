import copy
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1], [1, 1]]
        if numRows == 1:
            return [ans[0]]
        if numRows == 2:
            return ans
        i = 3
        while i != numRows+1:
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
        return ans
