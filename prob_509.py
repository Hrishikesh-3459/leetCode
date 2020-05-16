class Solution:
    def fib(self, N: int) -> int:
        if (N == 0):
            return 0
        a = 0
        b = 1
        lis_fib = [0,1]
        c = 0
        while (len(lis_fib) != N+1):
            c = a+b
            lis_fib.append(c)
            a = b
            b = c
        return(lis_fib[N])
