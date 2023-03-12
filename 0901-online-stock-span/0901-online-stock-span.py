class StockSpanner:

    def __init__(self):
        self.stocks = [[inf,-1]]
        self.index = -1
    def next(self, price: int) -> int:
        self.index += 1
        while price >= self.stocks[-1][0]:
            self.stocks.pop()
        
        self.stocks.append([price, self.index])
        return self.index - self.stocks[-2][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)