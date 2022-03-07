'''
[0,0,0]
 [24,1,0  [1,0,1],
1,24
24, 23
'''
import collections
from collections import deque
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # que=collections.deque([[0,0]])
        h=[]
        heapq.heappush(h,[grid[0][0],[0,0]])
        visited=set()
        visited.add((0,0))
        dirr=[(0,1),(0,-1),(1,0),(-1,0)]
        def isvalid(row,col): 
            return 0 <= row < len(grid) and 0 <=col<len(grid[0])
        # def minn(row,col):
        #     min=100000
        #     m=None
        #     for i in dirr:
        #         if isvalid(row+i[0],col+i[1]) and (row+i[0],col+i[1]) not in visited and ((grid[row + i[0]][col +i[1]] < min) or ((row +i[0]) == len(grid)-1 and (col +i[1])==len(grid[0])-1)):
        #             if (row +i[0] == len(grid)-1 and col +i[1]==len(grid[0])-1):
        #                 return [row + i[0], col +i[1]]                                                                  
        #             min=grid[row + i[0]][col +i[1]]
        #             m = [row+i[0],col+i[1]]
        #     if m:  
        #         # print(grid[m[0]][m[1]])
        #         return m
               
        max=grid[0][0]  
        while h:
            # cur=que.popleft()
            
            y=heappop(h)
            x=y[1]
#             print(grid[x[0]][x[1]])
#             print(x)
            
            if x and grid[x[0]][x[1]] > max:
                # print(1)
                max=grid[x[0]][x[1]]
                # print(max)
            
            if x and x[0]==len(grid)-1 and x[1]==len(grid[0])-1:
                return max
            if x: 
                for i in dirr:
                    if isvalid(x[0]+i[0],x[1]+i[1]) and (x[0]+i[0],x[1]+i[1]) not in visited:
                        heapq.heappush(h,[grid[x[0]+i[0]][x[1]+i[1]],[x[0]+i[0],x[1]+i[1]]]) 
                        visited.add((x[0]+i[0],x[1]+i[1]))
            
        return max    
            
            
            
            
            
           
