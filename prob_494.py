class Solution:
    def findTargetSumWays(self, nums, S):
        suma = sum(nums)
        if (S not in range(-1 * suma , suma + 1)):
            return 0
        if (S + suma ) % 2 != 0:
            return 0
        target = (S + suma) // 2
        return self.countSubsets(nums, target)
    
    def countSubsets(self, arr, target):
        n = len(arr)
        
        dp = [[0 for i in range(target + 1)]for j in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 1
            
        for i in range(1, n + 1):
            for j in range(0, target + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]