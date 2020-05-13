class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if (num == 0):
            return False
        power = []
        for i in range(25):
            power.append(4 ** i)
            if (num in power):
                return True
        return False
