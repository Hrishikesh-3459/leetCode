class Solution:
    def firstUniqChar(self, s: str) -> int:
        if (len(s) == 0):
            return -1
        new = []
        for i in s:
            if (i not in s[s.index(i)+1:len(s)]):
                new.append(i)
        if (len(new) == 0):
            return -1
        return(s.index(new[0]))
        
