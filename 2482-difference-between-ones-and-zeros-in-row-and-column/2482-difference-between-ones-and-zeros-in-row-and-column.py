class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        mem = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mem[(i,grid[i][j], "r")] += 1
                mem[(j,grid[i][j], "c")] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = mem[(i,1, "r")] + mem[(j,1, "c")] - mem[(i,0, "r")] - mem[(j,0, "c")]
        
        return grid