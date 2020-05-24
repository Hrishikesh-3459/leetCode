class Solution:
    def sortString(self, s: str) -> str:
        x = list(s)
        ans = []
        ans_2 = []
        fin = []
        count = 0
        while True:
            for i in sorted(x):
                if (i not in ans):
                    ans.append(i)
                    count +=1
                    x.pop(x.index(i))
            for j in sorted(x)[::-1]:
                if (j not in ans_2):
                    count +=1
                    ans_2.append(j)
                    x.pop(x.index(j))
            fin += ans + ans_2
            if (count == len(s)):
                break
            ans.clear()
            ans_2.clear()
        ans_str = ""
        for j in fin:
            ans_str += j
        return ans_str
