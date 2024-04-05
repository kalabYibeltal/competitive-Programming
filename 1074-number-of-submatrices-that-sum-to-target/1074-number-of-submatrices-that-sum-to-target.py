class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        pre = [[0 for y in range(len(matrix[0]) + 1)] for x in range(len(matrix) + 1)  ]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                        
                pre[i + 1][j + 1] = pre[i+1][j] + pre[i][j+1] - pre[i][j] + matrix[i][j]
        
        # print(pre)
        ans = 0
        for sc in range(len(matrix)):
            for ec in range(sc,len(matrix)):
                dic = defaultdict(int)
                dic[0] = 1
                for r in range(len(matrix[0])):
                    val = pre[ec+1][r+1] + pre[sc][0] - pre[sc][r+1] - pre[ec+1][0]
                    
                    ans += dic[val - target]
                    dic[val] += 1
                    # print(dic, val, r, sc, ec, ans)
                
                # print("------")
        
        return ans
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                
                
                