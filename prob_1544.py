class Solution:
    def makeGood(self, s):
        l = list(s)
        i = 0
        while True:
            if i + 1 == len(l):
                break
            if not l:
                break
            if (l[i] == l[i + 1].lower() or l[i].lower() == l[i + 1]) and l[i] != l[i + 1]:
                l.pop(i)
                l.pop(i)
                i = 0
            else:
                i += 1
        return ''.join(l)