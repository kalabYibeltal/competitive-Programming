class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = [0]
        for num in stones:
            prefix.append(prefix[-1] + num)
        
#         # print(prefix)
#         @lru_cache(None)
#         def dp(i,j,turn):
#             if turn == 1:
#                 if j == i:
#                     return 0
#                 return max(prefix[j+1] - prefix[i+1] + dp(i+1,j,0) , prefix[j] - prefix[i] + dp(i,j-1,0))
#             if j == i:
#                     return 0
#             return min(-(prefix[j+1] - prefix[i+1]) + dp(i+1,j,1) ,  -(prefix[j] - prefix[i]) + dp(i,j-1,1))
        
#         return dp(0,len(stones)-1,1)
        
        
        dp = [[[0 for i in range(len(stones))] for j in range(len(stones))] for k in range(2)]
        #0 for alice 1 for bob
        # print(dp)
        for line in range(1,len(stones)):
            for right in range(line, len(stones)):
                for turn in range(2):
                    left = right - line
                    dp[turn][left][right] =  max(prefix[right+1] - prefix[left+1] - dp[1-turn][left+1][right], prefix[right] - prefix[left] - dp[1-turn][left][right -1])
                    
                
                
        return dp[0][0][len(stones)-1]
        
        
        
        