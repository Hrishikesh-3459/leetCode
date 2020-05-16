class Solution:
    def reverseWords(self, s: str) -> str:
        x = []
        for i in s.split():
            x.append(i[::-1])
            
        y = ""
        for i in x:
            y += i + " "
        return y[:-1]
