class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if (N == 1):
            return 1
        di = {}
        noJ = []
        for i in trust:
            if (i[0] not in noJ):
                noJ.append(i[0])
            if(i[1] in di):
                di[i[1]] += 1
            else:
                di[i[1]] = 1
        mx = N-1
        for i in di:
            if (di[i] == mx and i not in noJ):
                return i
        return -1
                
