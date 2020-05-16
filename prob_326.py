def isPowerOfThree(self, n: int) -> bool:
        if (n == 0):
            return False
        power = []
        for i in range(50):
            power.append(3 ** i)
            if (n in power):
                return True
        return False
