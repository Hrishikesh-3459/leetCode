class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        num = 1
        while True:
            suma = num
            for i in nums:
                suma += i
                if (suma < 1):
                    num += 1
                    break
            if (suma >= 1):
                break
            
            
        return num
        
