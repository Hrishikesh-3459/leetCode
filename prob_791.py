class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans = ""
        for i in S:
            if i in T:
                ans += (i * T.count(i))
                T = T.replace(i, "")
        ans += T
        return ans
