class Solution:
    def sumOddLengthSubarrays(self, arr):
        ans = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr)):
                if i + j > len(arr):
                    break
                ans += sum(arr[j:j + i])
        return ans
