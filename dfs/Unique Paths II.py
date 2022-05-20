class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dictr = {}
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]==1: return 0
        def find(row,col):
            if row == len(obstacleGrid) or col == len(obstacleGrid[0]): return 0
            if obstacleGrid[row][col] == 1: return 0
            if (row == len(obstacleGrid) -1 and col == len(obstacleGrid[0])-1) :  return 1
            if (row,col) in dictr: return dictr[(row,col)]
            dictr[(row,col)] = find(row+1,col) + find(row, col +1)
            return dictr[(row,col)]
        
        return find(0,0)
        

        
