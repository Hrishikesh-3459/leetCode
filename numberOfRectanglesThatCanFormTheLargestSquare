class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        di = {}
        for l,w in rectangles:
            smol = min(l, w)
            if smol in di:
                di[smol] += 1
            else:
                di[smol] = 1
        big = max(list(di.keys()))
        return di[big]
