def trailingZeroes(n):
    i = n-1
    fact = n
    while(i > 1):
        fact *= i
        i -= 1
    return(str(fact).count('0'))

print(trailingZeroes(5))