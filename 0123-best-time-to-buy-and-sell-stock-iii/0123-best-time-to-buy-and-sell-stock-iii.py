class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ### georges answer
        @lru_cache(None)
        def rec(index,i,n):
            
            if n==0 or (index>=len(prices) ):
                return 0
            return max(i*prices[index]+rec(index+1,i*-1,n-1),rec(index+1,i,n))
        return max(rec(0,-1,4),0)
    
        
        @lru_cache(None)
        def dp(i,day,count):
        
            if day =="sell":
                if i == len(prices) - 1: return [prices[-1] , 0]
                arr = dp(i+1,"sell",count)
                prof = 0
                if count > 0: prof = dp(i+1,"buy",count)
                if prices[i]+prof>=  sum(arr):
                    return [prices[i],prof]
                return arr
            else:
                if count == 0: return 0
                if i == len(prices) - 1: return 0
                op1 = dp(i+1,"sell",count-1)
                op2 = dp(i+1,"buy",count)
                if (op1[0] - prices[i]) + op1[1] >= op2:
                    return (op1[0] - prices[i]) + op1[1]
                return op2
                
        return dp(0,"buy",2)