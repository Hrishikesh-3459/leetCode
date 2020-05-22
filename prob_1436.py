class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = []
        for i in paths:
            dest.append(i[1])
        for i in dest:
            flag = True
            for j in paths:
                if (i == j[0]):
                    flag = False
                    break
            if (flag == True):
                return i
