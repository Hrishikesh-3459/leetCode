class Solution:
    def isValid(self, s: str) -> bool:
        di = {")": "(", "}": "{", "]": "["}
        opening = ["(", "{", "["]
        sta = []
        for i in s:
            if i in opening:
                sta.append(i)
            else:
                if not sta:
                    return False
                x = sta.pop()
                if di[i] != x:
                    return False
        return not sta