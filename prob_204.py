class Solution:
    def countPrimes(self, n: int) -> int:
        if (n == 0 or n ==2):
            return 0
        val = [True for i in range(n+1)]
        p = 2
        while (p ** 2 < n):
            if (val[p] == True):
                for i in range(p * 2, n + 1, p):
                    val[i] = False
            p += 1
        val[0] = False
        val[1] = False
        count = 0
        for i in range(n):
            if (val[i] == True):
                count += 1
        return(count)
        
