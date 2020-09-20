class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        if spaces == 0:
            return text
        words = text.split()
        if len(words) == 1:
            x = words[0] + " " * (len(text) - len(words[0]))
            return x
        req = spaces // (len(words) - 1)
        extra = spaces % (len(words) - 1)
        ans = " " * req
        x = ans.join(words)
        return x + (" " * extra)
