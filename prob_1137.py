class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        trib = [a, b, c]
        if (n in [0, 1, 2]):
            return trib[n]
            
        while (len(trib) != n+1):
            d = a+b+c
            trib.append(d)
            a = b
            b = c
            c = d
        return trib[n]
        
