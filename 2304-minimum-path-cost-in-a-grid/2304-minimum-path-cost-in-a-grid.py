class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        
        @lru_cache(None)
        def dp(row, col):
            if row == len(grid) - 1:
                return grid[row][col]
            
            ans = inf
            for j in range(len(grid[0])):
                
                ans = min(ans, moveCost[grid[row][col]][j] + dp(row+1, j))
            
            return ans + grid[row][col]
        
        
        answer = inf
        for j in range(len(grid[0])):

            answer = min(answer, dp(0,j))
        
        return answer
        