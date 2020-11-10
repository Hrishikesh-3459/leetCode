# Get Maximum in Generated Array
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1] + ([0] * (n + 1))
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 0
        while True:
            if i == n:
                return max(nums)
            if 2 <= 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 <= 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
            i += 1
