class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        di = {}
        for i, num in enumerate(self.products):
            di[num] = self.prices[i]
        self.di = di
        self.counter = 0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        cost = 0
        for k,i in enumerate(product):
            val = (self.di[i] * amount[k])
            cost += val
        self.counter += 1
        if self.counter == self.n:
            cost = cost - (self.discount * cost) / 100
            self.counter = 0
        return cost

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
