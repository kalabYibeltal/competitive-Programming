class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(i,j):
            if not(0 <= j < len(matrix[0])):
                return inf
            
            if i == len(matrix) - 1:
                return matrix[i][j]
            
            return matrix[i][j] + min(dp(i+1,j), dp(i+1,j+1), dp(i+1,j-1))
        
        ans = inf
        for j in range(len(matrix[0])):
            ans = min(ans, dp(0,j))
        
        return ans