class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0 or len(s) == 0:
            return 0
        di = {}
        left = right = 0
        ans = 1
        while right < len(s):
            di[s[right]] = right
            if len(di) == k + 1:
                smol = min(di.values())
                del di[s[smol]]
                left = smol + 1
            right += 1
            ans = max(ans, right - left)
        return ans