class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            for j in range(len(s), -1, -1):
                if j > i and self.checknice(i, j, s):
                    ans.append(s[i:j])
        if ans:
            big = max(list(map(len, ans)))
        for i in ans:
            if len(i) == big:
                return i
        return ""
            
    def checknice(self, start, end, s):
        for i in range(start, end):
            if s[i].islower() and s[i].upper() not in s[start:end]:
                return False
            elif s[i].isupper() and s[i].lower() not in s[start:end]:
                return False
        return True
                
