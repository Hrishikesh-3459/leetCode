# Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums):
        suma = sum(nums)
        if suma & 1 == 1:
            return False
        return self.subset_sum(nums, suma // 2, len(nums))
    
    def subset_sum(self, arr, target, n):
        dp = [[False for i in range(target + 1)] for j in range(n + 1)]
        for i in range(target + 1):
            dp[0][i] = False
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j - arr[i - 1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][target]                           