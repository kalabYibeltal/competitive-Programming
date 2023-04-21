class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        prefix = [[0 for col in range(len(matrix[0])+1)] for row in range(len(matrix)+1)]
        
        for i in range(1,len(prefix)):
            for j in range(1,len(prefix[0])):
                prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + matrix[i-1][j-1] - prefix[i-1][j-1]
        
        
        count = 0
        for i in range(1,len(prefix)):
            for j in range(1,len(prefix[0])):
                
                for k in range(i,len(prefix)):
                    if j+(k-i) == len(prefix[0]):
                        break
                
                    if prefix[k][j+(k-i)] + prefix[i-1][j-1] - prefix[i-1][j+(k-i)] - prefix[k][j-1] == (k-i+1) * (k-i+1):
                        count += 1
                    
                    else:
                        break
        
        return count