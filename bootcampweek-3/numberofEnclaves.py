
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        marked =[ [ 0 for i in range(len(grid[0])) ] for j in range(len(grid)) ]
        # print(marked)
        i=0
        dirr=[(0,1),(0,-1),(-1,0),(1,0)]
        def isvalid(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0]) and (row,col) not in visited and grid[row][col]==1 
        
        def marker(row,col):
            for i in dirr:
                if isvalid(row+i[0],col+i[1]):
                    marked[row+i[0]][col+i[1]]=1
                    visited.add((row+i[0],col+i[1]))
                    marker(row+i[0],col+i[1])
                    
        while i<len(grid):
            j=0
            while j<len(grid[0]):
                if (i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1) and grid[i][j]==1:
                    # print([i,j])
                    marked[i][j]=1
                    visited.add((i,j))
                    marker(i,j)
                j+=1
            i+=1
        
       
        i=0
        count=0
        
        while i < len(grid):
            j=0
            while j<len(grid[0]):
                if marked[i][j]==0 and grid[i][j]==1:
                    count+=1
                j+=1
            i+=1
        return count
