class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = [0] * len(S)
        for i, let in enumerate(S):
            if not let.isalpha():
                ans[i] = let
        for i, let in enumerate(S[::-1]):
            if let.isalpha():
                ind = ans.index(0)
                ans[ind] = let
        fin = ""
        for i in ans:
            fin += i
        return fin
