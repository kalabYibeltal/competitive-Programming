class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [x*x for x in range(316, 0, -1)]  
        
        @lru_cache(None)
        def dp(n,t):
            if n == 0:
                if t == 0:
                    return True
                return 
            if t == 1:
                ans = False
                for x in squares:
                    if x <= n:
                        ans = ans or dp(n-x,1-t)
            
            else:
                ans = True
                for x in squares:
                    if x <= n:
                        ans = ans and dp(n-x,1-t)
            
            return ans
        
        
        return dp(n,1)
    
    
    
    
