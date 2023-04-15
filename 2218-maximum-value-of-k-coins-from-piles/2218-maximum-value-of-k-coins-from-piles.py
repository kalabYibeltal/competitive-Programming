class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @lru_cache(None)
        def dp(k,index):
            # print(k,index)
            if k == 0 or index == len(piles):
                return 0
            ans = dp(k,index + 1)
            su = 0
            for i in range(len(piles[index])):
                if k == 0:
                    break
                
                su += piles[index][i]
                k -= 1 
                ans = max(ans, su + dp(k,index + 1))
            
            return ans
        
        return dp(k,0)