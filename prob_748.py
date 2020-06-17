class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        di = []
        for i in licensePlate:
            if not i.isalpha():
                continue
            di.append(i.lower())
        ans = []
        smol = 10001
        for i in words:
            cp = i
            flag = False
            for j in di:
                if j in i:
                    i = i.replace(j, "", 1)
                elif j not in i:
                    flag = True
                    break
            if flag == False:
                ans.append(cp)
                cur = len(cp)
                smol = min(smol, cur)
        for i in ans:
            if len(i) == smol:
                return i
