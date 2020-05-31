class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        x = list(s)
        for i in range(0, len(x), 2*k):
            x[i : i + k] = reversed(x[i : i + k])
        return "".join(x)
