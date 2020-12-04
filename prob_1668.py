class Solution:
    def maxRepeating(self, sequence, word):
        ans = 1
        while True:
            if (word * ans) in sequence:
                ans += 1
            else:
                return ans - 1
