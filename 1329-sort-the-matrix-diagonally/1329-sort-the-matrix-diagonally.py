class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        arrs = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arrs[j-i].append(mat[i][j])
        
        for key in arrs:
            arrs[key].sort()
            i, j = -key, 0
            if key > 0:
                j = key
                i = 0
            for elem in arrs[key]:
                mat[i][j] = elem
                i += 1 
                j += 1
        
        return mat
            
            
            
            
            
            
            