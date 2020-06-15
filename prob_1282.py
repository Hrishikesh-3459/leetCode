class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        di = {}
        for i, per in enumerate(groupSizes):
            if per in di:
                di[per].append(i)
            else:
                di[per] = [i]
        ans = []
        for i in di:
            tmp = []
            while di[i]:
                for j in range(i):
                    tmp.append(di[i].pop())
                x = sorted(tmp)
                ans.append(x)
                tmp.clear()
        return ans
