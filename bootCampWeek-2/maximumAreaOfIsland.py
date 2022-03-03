
def mark(board,row,col,visited,maxx):
    if row+1 < len(board) and visited[row+1][col]==0 and  board[row+1][col]==1:
        maxx.append(1)
        visited[row+1][col]=1
        mark(board,row+1,col,visited,maxx)
    if col+1 < len(board[0]) and visited[row][col+1]==0  and  board[row][col+1]==1:
        maxx.append(1)
        visited[row][col+1]=1
        mark(board,row,col+1,visited,maxx)
   
    if col-1 >= 0 and visited[row][col-1]==0  and  board[row][col-1]==1:
        maxx.append(1)
        visited[row][col-1]=1
        mark(board,row,col-1,visited,maxx)
    if row-1 > -1 and visited[row-1][col]==0  and  board[row-1][col]==1:
        maxx.append(1)
        visited[row-1][col]=1
        mark(board,row-1,col,visited,maxx)
    



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      
        visited = [ [ 0 for i in range(len(grid[0])) ] for j in range(len(grid)) ]
        maxx=[]
        x=0
        i=0
        while i < len(grid):
            j=0
            while j < len(grid[0]):
                if grid[i][j]==1 and visited[i][j]==0:
                    visited[i][j]=1
                    maxx.append(1)
                    mark(grid,i,j,visited,maxx)
                    
                    if len(maxx) > x:
                        x=len(maxx)
                    maxx=[]
                j+=1
            i+=1
        return x
      
