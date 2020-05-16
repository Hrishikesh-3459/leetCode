<<<<<<< HEAD
def firstUniqChar(s):
    new = []
    for i in s:
        if (i not in s[s.index(i)+1:len(s)]):
            new.append(i)
    if (new[0] in s):
        return(s.index(new[0]))
    else :
        return -1

print(firstUniqChar("leetcode"))
=======
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
        
>>>>>>> c342f33c5f94635b5901867b435c2165820ee334
