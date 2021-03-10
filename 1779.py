class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid = []
        for p in points:
            if p[0] == x or p[1] == y:
                valid.append(p)
        if not valid:
            return -1
        min_dist = float('inf')
        ans = -1
        for i,p in enumerate(valid):
            dist = abs(p[0] - x) + abs(p[1] - y)
            if dist < min_dist:
                min_dist = dist
                ans = points.index(p)
        return ans
                
