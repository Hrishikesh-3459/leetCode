class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones:
            if len(stones) == 1:
                return stones[0]
            big1 = max(stones)
            stones.remove(big1)
            big2 = max(stones)
            stones.remove(big2)
            if big1 == big2:
                continue
            else:
                new = big1 - big2
                stones.append(new)
        return 0
