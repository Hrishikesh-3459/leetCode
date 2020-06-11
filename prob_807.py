class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_cols = list(map(max, zip(*grid)))
        max_rows = list(map(max, grid))
        ans = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                val = min(max_rows[i], max_cols[j])
                ans += abs(col - val)
        return ans
