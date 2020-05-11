 def trailingZeroes(self, n):
        
        return 0 if n == 0 else int(n / 5 + self.trailingZeroes(n / 5))
        # if (n == 0):
        #     return (0)
        # i = n-1
        # fact = n
        # while(i > 1):
        #     fact *= i
        #     i -= 1
        # return(len(str(fact)) - len(str(fact).rstrip('0')))

