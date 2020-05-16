<<<<<<< HEAD
def trailingZeroes(n):
    i = n-1
    fact = n
    while(i > 1):
        fact *= i
        i -= 1
    return(str(fact).count('0'))

print(trailingZeroes(5))
=======
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

>>>>>>> c342f33c5f94635b5901867b435c2165820ee334
