class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def isvalid(row,col): return 0<= row < len(mat) and 0<= col < len(mat[0])
        ans =[]
        for i in range(len(mat)):
            ans.append([0]*len(mat[0]))
            
        suma = 0
        for i in range(-k,k+1):
            for j in range(-k,k+1):
                if isvalid(i,j): suma += mat[i][j]
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j == 0: 
                    ans[i][0] = suma
                    sumb = suma
                else: 
                    for p in range(-k,k+1):
                        if isvalid(i + p ,j-k-1): 
                            sumb -= mat[i + p][j-k-1]
        
                    for p in range(-k,k+1):
                        if isvalid(i + p ,j+k): 
                            sumb += mat[i + p][j+k]
                
                        
                    ans[i][j] = sumb
            
            # print(suma)
            for p in range(-k,k+1):
                if isvalid(i - k  ,p): suma -= mat[i - k ][p]
        
            for p in range(-k,k+1):
                if isvalid(i + k + 1 , p): suma += mat[i + k +1][p]
            
            # print(suma)
                    
        
        return ans
