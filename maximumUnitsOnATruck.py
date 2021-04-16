class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = sorted(boxTypes, key = (lambda x: x[-1]), reverse = True)
        ans = 0
        for b, u in arr:
            if b > truckSize:
                ans += (truckSize * u)
                break
            else:
                truckSize -= b
                ans += (b * u)
        return ans
