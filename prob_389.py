class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x =list(t)
        for i in s:
            x.remove(i)

        return(x[0])
            
