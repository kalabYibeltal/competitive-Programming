class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited= set()
        def valid(row,col): return 0 <= row < len(board) and 0 <= col <  len(board[0]) 
        dir = [(0,1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]
        def revlr(row,col):
            visited.add((row,col))
            count = 0
            for i in dir:
                if valid(row+i[0],col+i[1]) and board[row+i[0]][col+i[1]] == 'M': count +=1
                # if (row+i[0])==2 and (col + i[1]) == 3: print(count)
            if board[row][col] == 'M':
                board[row][col] = 'X'
                
            elif count == 0:
               
                board[row][col] = 'B'
                for i in dir:
                    if valid(row+i[0],col+i[1]) and (row+i[0],col+i[1]) not in visited :
                        revlr(row+i[0],col+i[1])

            else: board[row][col] = str(count)
  
        revlr(click[0],click[1])
        return board
