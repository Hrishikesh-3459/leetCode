class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            s1 = s[:i+1]
            s2 = s[i+1:]
            if (len(s1) == 0 or len(s2) == 0):
                continue
            temp_ans = s1.count('0') + s2.count('1')
            if (temp_ans > ans):
                ans = temp_ans
        
        return ans
            
