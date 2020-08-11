class Solution:
    def removeVowels(self, S):
        for i in ('a', 'e', 'i', 'o', 'u'):
            S = S.replace(i,"")
        return S