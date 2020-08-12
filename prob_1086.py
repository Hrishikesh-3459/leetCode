class Solution:
    def highFive(self, items):
        di = {}
        for i, j in items:
            if i in di:
                di[i].append(j)
            else:
                di[i] = [j]
        ans = []
        for i in di:
            tmp = [i]
            val = sorted(di[i], reverse = True)
            fin = sum(val[:5]) // 5
            tmp.append(fin)
            ans.append(tmp)
        return ans