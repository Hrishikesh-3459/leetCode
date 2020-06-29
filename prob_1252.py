class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0 for i in range(m)] for j in range(n)]
        for r, c in indices:
            for i in range(m):
                mat[r][i] += 1
            for i in range(n):
                mat[i][c] += 1
        ans = 0
        for r in mat:
            for c in r:
                if c % 2 == 1:
                    ans += 1
        return ans
