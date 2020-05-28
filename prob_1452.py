class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        dic = {}
        j = 0
        for i in favoriteCompanies:
            dic[j] = i
            j += 1
        ans = []
        for i in favoriteCompanies:
            flag = 0
            for j in dic:
                if (set(i).issubset(dic[j])):
                    flag += 1
            if (flag == 1):
                ans.append(favoriteCompanies.index(i))
        return ans
        
        
