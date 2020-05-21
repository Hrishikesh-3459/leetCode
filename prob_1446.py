class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        max_len = 0
        while (i < len(s)):
            cur = s[i]
            le = 0
            for j in s[i:]:
                if (j != cur):
                    break
                else:
                    le += 1
            if (le > max_len):
                max_len = le
            i += 1
        return max_len
