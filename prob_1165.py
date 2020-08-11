class Solution:
    def calculateTime(self, keyboard, word):
        di = {}
        for i,j in enumerate(keyboard):
            di[j] = i
        ans = di[word[0]]
        for i in range(1, len(word)):
            val = abs(di[word[i - 1]] - di[word[i]])
            ans += val
        return ans