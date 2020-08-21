class Solution:
    def shortestCommonSupersequence(self, a, b):
        m = len(a)
        n = len(b)
        dp = [[0 for i in range(n + 1)]for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i = m
        j = n
        s = ""
        while i > 0 and j > 0:
            if a[i - 1] == b[j - 1]:
                s += a[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                s += a[i - 1]
                i -= 1
            else:
                s += b[j - 1]
                j -= 1
        while i > 0:
            s += a[i - 1]
            i -= 1
        while j > 0:
            s += b[j - 1]
            j -= 1
        return s[::-1]