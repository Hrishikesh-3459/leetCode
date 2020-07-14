def findMinFibonacciNumbers(k):
    fib = [1,1]
    while fib[-1] <= k:
        val = fib[-1] + fib[-2]
        fib.append(val)
    ans = 0
    while k > 0:
        num = fib.pop()
        if num <= k:
            k -= num
            ans += 1
    return ans