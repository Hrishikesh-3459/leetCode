import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if (num <= 0):
            return False
        lim = math.sqrt(num)
        suma = 0
        for i in range(1, int(lim)+1):
            if num % i == 0:
                suma += i
                if i ** 2 != num:
                    suma += num // i
        return suma - num == num
        
