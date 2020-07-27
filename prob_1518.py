def numWaterBottles(numBottles, numExchange):
    n = numBottles
    ans = 0
    rem = 0
    while n > 0:
        ans += n
        n += rem
        rem = n % numExchange
        n //= numExchange
    return ans