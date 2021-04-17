class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        ans = ""
        while True:
            if word1:
                ans += word1.pop(0)
            else:
                ans += ''.join(word2)
                break
            if word2:
                ans += word2.pop(0)
            else:
                ans += ''.join(word1)
                break
        return ans
