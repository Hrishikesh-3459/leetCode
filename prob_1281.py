class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        suma = 0
        for i in str(n):
            suma += int(i)
            pro *= int(i)
        return (pro - suma)
        
