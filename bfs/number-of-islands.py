class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirr = [[0,1],[1,0],[-1,0],[0,-1]]
        def isvalid(row,col): return 0<= row < len(grid) and 0<= col < len(grid[0]) and (row,col) not in visited and grid[row][col] == "1"
        visited = set()
        def mark(row,col):
            que = collections.deque([[row,col]])
            while que:
                row, col = que.popleft()
                for i in dirr:
                    if isvalid(row + i[0], col + i[1]):
                        que.append([row + i[0], col + i[1]])
                        visited.add((row + i[0],col + i[1]))
            
        
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if isvalid(i,j): 
                    mark(i,j)
                    counter += 1
            
        return counter
