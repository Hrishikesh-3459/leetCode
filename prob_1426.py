class Solution:
    def countElements(self, arr):
        ans = 0
        for i in arr:
            if i + 1 in arr:
                ans += 1
        return ans