class Solution:
    def checkStraightLine(self, coordinates):
        prev = None
        for i in range(1, len(coordinates)):
            cur = self.slope(
                coordinates[i][1], coordinates[i - 1][1], coordinates[i][0], coordinates[i - 1][0])
            if prev != None and cur != prev:
                return False
            prev = cur
        return True

    def slope(self, y2, y1, x2, x1):
        try:
            return (y2 - y1) / (x2 - x1)
        except:
            return float('inf')
