class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        q = list(s)
        for i in t:
            if i == q[0]:
                q.pop(0)
            if not q:
                return True
        if q:
            return False
        return True
