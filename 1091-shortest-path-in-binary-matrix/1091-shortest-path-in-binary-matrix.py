class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        dirr = [(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        def isvalid(row,col): return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row,col) not in visited and grid[row][col] == 0
        visited = set()
        que = deque([[0,0,1]])
        visited.add((0,0))
        if grid[0][0] != 0: return -1
        while que:
            row,col,lev = que.popleft()
            if row == len(grid)-1 and col == len(grid[0])-1: return lev
            for i in dirr:
                if isvalid(row+i[0],col+i[1]):
                    que.append([row+i[0],col+i[1],lev+1])
                    visited.add((row+i[0],col+i[1]))
        
        return -1