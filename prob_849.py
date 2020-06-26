class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        cur = 0
        ans = 0
        while i < len(seats):
            if seats[i] == 0:
                cur += 1
            else:
                tmp = (cur + 1) // 2
                ans = max(ans, tmp)
                cur = 0
            i += 1
        return max(ans, seats.index(1), seats[::-1].index(1))
