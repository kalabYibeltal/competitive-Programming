class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = inf
        bi = 0
        s = 0
        si = 0
        profit = 0
        for i in range(0,len(prices)):
            if prices[i] > s and i > bi:
                # print(i)
                si = i
                s = prices[i]
                if s-b > profit: profit = s -b
            if prices[i] < b:
                # print(i)
                bi = i
                b = prices[i]
                if si < bi: s = 0
        return profit
            
