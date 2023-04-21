class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        
        @lru_cache(None)
        def dp(n,profite,index):
            if index == len(group) or n == 0:
                if profite >= minProfit:
                    return 1
                return 0
            
            ans = dp(n,profite, index + 1)
            if n >= group[index]:
                ans += dp(n-group[index], min(minProfit, profite + profit[index]),index+1)
            
            return ans
        
        return dp(n,0,0) % 1000000007