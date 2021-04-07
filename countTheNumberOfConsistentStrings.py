class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        ans = 0
        for word in words:
            flag = True
            for letter in word:
                if letter not in allowed:
                    flag = False
                    break
            if flag == True:
                ans += 1
        return ans
