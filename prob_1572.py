class Solution:
    def diagonalSum(self, mat) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            # print(f"{(i,i)} != {(i,n - i - 1)}")
            if (i, i) != (i, n - i - 1):
                ans += mat[i][n-i-1]
        return ans
