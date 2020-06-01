class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x = sorted(p)
        k = len(p)
        i = 0
        ans = []
        while True:
            if (i + k > len(s)):
                break
            c = s[i : i + k]
            if (sorted(c) == x):
                ans.append(i)
            i += 1
        return ans
