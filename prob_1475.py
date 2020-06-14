class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        k = 0
        for i, n in enumerate(prices):
            flag = True
            for j, v in enumerate(prices[i + 1: ]):
                if v <= n:
                    flag = False
                    val = n - v
                    ans.append(val)
                    break
            if flag == True:
                ans.append(n)
        return ans
