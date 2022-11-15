class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirr = [[1,0],[1,-1],[1,1],[0,1],[0,-1],[-1,0],[-1,-1],[-1,1]]
        
        def isvalid(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def count(row,col):
            countf = 0
            for dx, dy in dirr:
                if isvalid(row + dx, col + dy):
                    if board[row + dx][col + dy] == 1 or board[row + dx][col + dy] == 0.5:
                        countf += 1
            
            return countf
        
        for i in range(len(board)):
            for j in range(len(board[0])): 
                c = count(i,j)
                if board[i][j] == 1 and (c < 2 or c >3):
                    board[i][j] = 0.5
                if board[i][j] == 0 and c == 3:
                    board[i][j] = 1.5
        
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = int(board[i][j])
                    