class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # brute force
        # row, (r1, r2) =row - 1 (r1 *3, r2*2 )
        #[ r1       r2         ]
        #[r1r1r1  r2r2r2       ]
        # 70 * 35 * 35=  ~  1.5 * 10^5
        # time o(n^3) n == no of rows or cols
        # number rows * (numbers cols ^ 2)
        
        @lru_cache(None)
        def dp(row, pos_r1, pos_r2):
            if row == len(grid) - 1:
                if pos_r1 == pos_r2:
                    return grid[row][pos_r1]    
                
                return grid[row][pos_r1] + grid[row][pos_r2]
            
            max_val = 0
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if 0 <= pos_r1 + i < len(grid[0]) and 0 <= pos_r2 + j < len(grid[0]):
                        max_val = max(max_val, dp(row+1, pos_r1 + i, pos_r2 + j))
            
            if pos_r1 == pos_r2:
                return grid[row][pos_r1] + max_val 
            
            return max_val + grid[row][pos_r1] + grid[row][pos_r2]
        
        
        return dp(0, 0, len(grid[0]) -1)
        
        # [[2,3]
        # [[3, 5]]
     