class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        x = str.split()
        if (len(x) != len(pattern)):
            return False
        di = {}
        y = 0
        for i in pattern:
            di[i] = x[y]
            y += 1
        z = 0
        l = []
        for i in di:
            if (di[i] not in l):
                l.append(di[i])

        if (len(di) != len(l)):
            return False
        for i in pattern:
            if (di[i] != x[z]):
                return False
            z += 1
        return True
                
