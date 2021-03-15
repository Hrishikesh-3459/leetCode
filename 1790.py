class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return False
        if s1 == s2:
            return True
        d = []
        k = 0
        for i, j in zip(s1, s2):
            if i != j:
                d.append(k)
            k += 1
        if len(d) != 2:
            return False
        p = list(s1)
        p[d[0]], p[d[1]] = p[d[1]], p[d[0]]
        if ''.join(p) != s2:
            return False
        return True
