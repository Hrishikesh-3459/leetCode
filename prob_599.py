class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        andy = {}
        resto = set()
        for i, cho in enumerate(list1):
            andy[cho] = i
            resto.add(cho)
        doris = {}
        for i,cho in enumerate(list2):
            doris[cho] = i
            resto.add(cho)
        ans = {}
        for i in list(resto):
            if i in andy and i in doris:
                val = andy[i] + doris[i]
                ans[i] = val
        smol = min(ans.values())
        fin = []
        for i in ans:
            if ans[i] == smol:
                fin.append(i)
        return fin
