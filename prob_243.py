class Solution:
    def shortestDistance(self, words, word1, word2):
        ans = float('inf')
        ind1 = []
        ind2 = []
        for i, n in enumerate(words):
            if n == word1:
                ind1.append(i)
            elif n == word2:
                ind2.append(i)
        for i in ind1:
            for j in ind2:
                ans = min(ans, abs(i - j))
        return ans
        