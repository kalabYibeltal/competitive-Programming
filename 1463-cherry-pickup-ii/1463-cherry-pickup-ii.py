class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        # def isValid(col):
            # return 0 <= col < len(grid[0])
        
        @lru_cache(None)
        def topDown(row,col1,col2):
            
            if row == len(grid) or col1 < 0 or col1 == len(grid[0]) or col2 < 0 or col2 == len(grid[0]):
                return 0
            Max = 0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    Max = max(Max,topDown(row+1,col1+i,col2+j))
            
            return grid[row][col1] + grid[row][col2] - ((col1==col2)==True)*grid[row][col2] + Max
        
        return topDown(0,0,len(grid[0])-1)
                
            