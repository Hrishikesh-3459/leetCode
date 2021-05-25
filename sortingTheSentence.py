class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        di = {}
        for word in s.split():
            l = len(word)
            pos = word[l - 1]
            di[int(pos)] = word[:l-1]
        ans = ""
        for i in range(1, len(s.split()) + 1):
            ans += di[i] + " "
        ans = ans.strip()
        return ans
