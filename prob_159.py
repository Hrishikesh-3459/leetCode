class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if len(s) == 0:
            return 0
        if len(set(s)) == 2:
            return len(s)
        di = {}
        ans = 0 #0,1
        left = right = 0
        while right < len(s):
            di[s[right]] = right
            if len(di) == 3:
                smol = min(di.values())
                del di[s[smol]]
                left = smol + 1
            right += 1
            ans = max(ans, right - left)
        return ans