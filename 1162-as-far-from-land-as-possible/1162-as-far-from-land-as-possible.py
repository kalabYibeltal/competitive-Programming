class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        

        dist = [[inf for _ in range(len(grid[0]))] for __ in range(len(grid))]
    
        
        ####should have started from all 1s at same time not independently
        def path_finder(i,j):
            que = deque()
            que.append([i,j,0])
            

            while que:
                row, col, cost = que.popleft()
            
                for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                    if row +dx < 0 or col+dy < 0 or row+dx >= len(grid) or col+dy >= len(grid[0]):
                        continue
                    if grid[row+dx][col+dy] == 0:
                        if cost + 1 < dist[row+dx][col+dy]:
                            dist[row+dx][col+dy] = cost + 1
                            que.append([row+dx, col+dy, cost + 1])

       
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    path_finder(i,j)
                    
        
        solution = max([max(row) for row in dist])
        return solution if 0 < solution < inf else -1
            
        
        ### internet clean solution    
        n = len(grid)
        q = []
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def isvalid(i,j):
            if 0<=i<n and 0<=j<n and grid[i][j]==0:
                return True
            return False

        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
                    dp[i][j]=0

        res = -1
        while q:
            x,y = q.pop(0)
            for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
                if isvalid(x+dx,y+dy) and dp[x+dx][y+dy]==-1:
                    q.append((x+dx,y+dy))
                    dp[x+dx][y+dy] = dp[x][y]+1
                    res = max(res,dp[x+dx][y+dy])

        return res