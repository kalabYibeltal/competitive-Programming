class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buydict = {}
        selldict = {}
        def buy(i):
            if i in buydict: return buydict[i]
            maxx = 0
            for j in range(i+1, len(prices)):
                profit = sell(i, j)
                if profit > maxx:
                    maxx = profit
            ans = maxx 
            buydict[i] = ans
            return ans
        
        def sell(k, i):
            if i in selldict: return selldict[i] + (prices[i] - prices[k])
            maxx = 0
            for j in range(i+2, len(prices)):
                profit = buy(j)
                if profit > maxx:
                    maxx = profit
            selldict[i] = maxx
            return maxx + (prices[i] - prices[k])
       
        maxprofit = 0
        for k in range(0, len(prices)):
            x =  buy(k)
            if x > maxprofit: maxprofit = x
        return maxprofit
