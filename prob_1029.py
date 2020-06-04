class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tot = 0
        ref = []
        for i in costs:
            tot += i[0]
            ref.append(i[1] - i[0])
        x = sorted(ref)
        for i in range(len(costs)//2):
            tot += x[i]
        return tot
        
