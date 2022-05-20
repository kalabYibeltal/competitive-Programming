class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dictr = {}
        visited = set()
        dirc = [[0,1],[0,-1],[-1,0],[1,0]]
        def valid(row,col): return 0<= row< len(matrix) and 0<=col<len(matrix[0])
            
        def find(row,col):
            
            val = 0
            for i in dirc:
                if valid(row + i[0], col +i[1]) :
                    if matrix[row + i[0]][col + i[1]] > matrix[row][col]:
                        if((row + i[0], col + i[1])) in dictr: 
                            val = max(val, dictr[(row + i[0], col + i[1])])
                        else: val = max(val, find(row + i[0], col +i[1]))
                        
            dictr[(row,col)] = val + 1
            return val + 1
                
        # return find(2,3)   
    
    
        ans = 0    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited = set()
                ans  = max(ans,find(i,j))
        
        return ans
