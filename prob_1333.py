class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = {}
        if veganFriendly == 1:
            vf = True
        else:
            vf = False
        for i in restaurants:
            idi = i[0]
            ret = i[1]
            if vf:
                if i[2] == 0:
                    continue
            if i[3] <= maxPrice and i[4] <= maxDistance:
                if ret in ans:
                    ans[ret].append(idi)
                else:
                    ans[ret] = [idi]
        fin = []
        for i in sorted(ans):
            if len(ans[i]) == 1:
                fin.append(ans[i][0])
            else:
                for j in sorted(ans[i]):
                    fin.append(j)
        return fin[::-1]
