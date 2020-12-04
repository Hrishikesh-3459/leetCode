class Solution:
    def maximumWealth(self, accounts) -> int:

        # return max(map(sum, accounts))

        ans = 0
        for person in accounts:
            tmp = 0
            for bank in person:
                tmp += bank
            ans = max(ans, tmp)
        return ans
