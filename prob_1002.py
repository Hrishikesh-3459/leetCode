class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        l = list(map(list, A))
        l.pop(0)
        for i in A[0]:
            flag = True
            for j in l:
                if (i not in j):
                    flag = False
                    break
            if (flag == True):
                ans.append(i)
                for j in l:
                    j.remove(i)
                # print(l)
        return ans
