import copy
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for i in range(1, len(searchWord)+1):
            x = searchWord[:i]
            tmp = []
            for j in products:
                if j.startswith(x):
                    tmp.append(j)
                if len(tmp) == 3:
                    break
            t = copy.copy(tmp)
            ans.append(t)
            tmp.clear()
        return ans
