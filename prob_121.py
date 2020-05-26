 profit = 0
        if (len(prices) == 0 or len(prices) == 1):
            return 0
        smol = prices[0]
        big = prices[0]
        for num in prices[1:]:
            if (num < smol):
                smol = num
                big = num
            elif (num > big):
                big = num
            if(profit < (big - smol)):
                profit = big - smol
                
        return (profit)
