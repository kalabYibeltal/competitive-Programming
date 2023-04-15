class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def dp(total, index):
            if total == amount:
                return 1
            if index == len(coins):
                return 0
            
            answer = dp(total, index + 1)
            
            while total + coins[index] <= amount:
                
                total += coins[index]
                answer += dp(total, index + 1)
            
            return answer
        
        return dp(0, 0)