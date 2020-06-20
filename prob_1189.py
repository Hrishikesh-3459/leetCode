class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        di = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in text:
            if i in di:
                di[i] += 1
        for i in di:
            if di[i] == 0:
                return 0
        if di['b'] == di['a'] == di['n'] == di['l'] // 2 == di['o'] // 2:
            return di['b']
        val = min(di['b'], di['a'], di['o'], di['l'] // 2, di['o'] // 2)
        return val
