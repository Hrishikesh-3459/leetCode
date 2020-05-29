class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(set(s)) != len(set(t))):
            return False
        di = {}
        for i in range(len(s)):
            if (s[i] not in di):
                di[s[i]] = t[i]
            else:
                if (di[s[i]] != t[i]):
                    return False
                
        return True
                
        
