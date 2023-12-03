class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def dp(prev, i, prevC):
            if i == len(days):
                return 0
            
            if days[i] - days[prev] >= prevC:
                ans = inf
                
                ans = min(ans, dp(i,i+1, 1) + costs[0])
                ans = min(ans, dp(i,i+1, 7) + costs[1])
                ans = min(ans, dp(i,i+1, 30) + costs[2])
            
                return ans
            
            return dp(prev, i+1, prevC)
        
        return dp(0,0,0)
                
                