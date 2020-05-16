class Solution:
    def checkRecord(self, s: str) -> bool:
        if (s.count('A') > 1):
            return False
        i = 0
        l_count = 0
        while (i < len(s)):
            if (s[i] == 'L'):
                l_count += 1
                if (l_count > 2):
                    return False
            else:
                if (l_count > 2):
                    return False
                l_count = 0
            i += 1
        return True
        
