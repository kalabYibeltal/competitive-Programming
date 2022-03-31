class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dictr = {}
        def path(row,col):
            if row == len(grid) or col == len(grid[0]): return inf
            if row == len(grid)-1 and col == len(grid[0])-1:
                return grid[row][col]
            if (row,col) in dictr: return dictr[(row,col)]
            else:
                ans = min(path(row+1,col), path(row,col+1)) + grid[row][col]
                dictr[(row,col)] = ans
                return ans
        return path(0,0)
