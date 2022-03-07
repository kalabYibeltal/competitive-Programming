import collections
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        min=1000000
        i=0
        visited=set()
        def isvalid(row,col):
            return row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and (row,col) not in visited 
        dirr=[(0,1),(0,-1),(1,0),(-1,0)]
        x=True
        p=False
        while i < len(grid):
            j=0
            while j<len(grid[0]):
                if grid[i][j]==2:
                    if not x:
                        # print(j)
                        que.append([i,j])
                        time.append(0)
                        visited.add((i,j))
                        p=True
                    else:
                        que = collections.deque([[i,j]])
                        time = collections.deque([0])
                        visited.add((i,j))
                        p=True
                        x=False
                j+=1
            i+=1
        tl=0
        while p and que:
            cur=que.popleft()
            t=time.popleft()
            # print(cur)
            for d in dirr:
                # print(d)
                if isvalid(cur[0]+d[0],cur[1]+d[1]) and grid[cur[0]+d[0]][cur[1]+d[1]]==1:
                    visited.add((cur[0]+d[0], cur[1]+d[1]))
                    que.append([cur[0]+d[0], cur[1]+d[1]])
                    time.append(t+1)
                    
                    tl=t+1
        m=True
        i=0
        while i<len(grid):
            j=0
            while j<len(grid[0]):
                if (i,j) not in visited and grid[i][j]==1:
                    m=False
                j+=1
            i+=1
        if m: return tl
        return -1
        
        
        


        
        
        
        
        
        
