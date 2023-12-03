class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
#         mem = defaultdict(int)
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 mem[(i,grid[i][j], "r")] += 1
#                 mem[(j,grid[i][j], "c")] += 1
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 grid[i][j] = mem[(i,1, "r")] + mem[(j,1, "c")] - mem[(i,0, "r")] - mem[(j,0, "c")]
        
        # return grid
    
        ### online sub
        m, n = len(grid), len(grid[0])
        def count(nums) : return 2*sum(nums)-len(nums)       # [1] count score for a list of numbers
            
        rows = list(map(count, grid))                        # [2] count scores for rows
        cols = list(map(count, zip(*grid)))                  # [3] count scores for columns (transpose)

        for i,j in product(range(m), range(n)):              # [4] update the input matrix with
            grid[i][j] = rows[i] + cols[j]                   #     sums of precomputed scores
                
        return grid