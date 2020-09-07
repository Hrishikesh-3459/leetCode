class Solution:
    def modifyString(self, s: str) -> str:
        cur = 97
        ans = ""
        for i, n in enumerate(s):
            if n == '?':
                if len(s) == 1:  # Special case, when the string is only one question mark
                    return chr(cur)
                if i == 0:
                    while chr(cur) == s[i + 1]:
                        cur += 1
                        if cur == 123:
                            cur = 97
                    ans += chr(cur)
                elif i == len(s) - 1:
                    while chr(cur) == s[-2]:
                        cur += 1
                        if cur == 123:
                            cur = 97
                    ans += chr(cur)
                else:
                    while chr(cur) == s[i - 1] or chr(cur) == s[i + 1]:
                        cur += 1
                        if cur == 123:
                            cur = 97
                    ans += chr(cur)
                cur += 1
            else:
                ans += n
        return ans
