class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if (n == 1):
            return True
        x = "{0:b}".format(n)
        i = 0
        if (x[-1] == x[-2]):
            return False
        while True:
            if (i+1 == len(x)):
                break
            if (x[i] == x[i+1]):
                return False
            i += 1
        return True
            
        
