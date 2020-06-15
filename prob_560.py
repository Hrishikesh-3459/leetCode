class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di = {0: 1}
        suma = 0
        count = 0
        for i in nums:
            suma += i
            if (suma - k) in di:
                count += di[suma - k]
            di[suma] = di.get(suma, 0) + 1
        return count
