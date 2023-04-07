class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        prefix = [[0 for col in range(len(pizza[0])+1)] for row in range(len(pizza)+1)]
        for i in range(1,len(prefix)):
            for j in range(1,len(prefix[0])):
                prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + (pizza[i-1][j-1]== 'A') - prefix[i-1][j-1]
        @lru_cache(None)
        def dp(r,c,k):
            if k == 1:
                return prefix[len(pizza)][len(pizza[0])] + prefix[r][c] - prefix[r][len(pizza[0])] - prefix[len(pizza)][c] > 0
            ans = 0            
            for i in range(r+1, len(pizza)):
                val = prefix[i][len(pizza[0])] + prefix[r][c] - prefix[r][len(pizza[0])] - prefix[i][c] > 0
                # print(val,r,c,i)
                if prefix[i][len(pizza[0])] + prefix[r][c] - prefix[r][len(pizza[0])] - prefix[i][c] > 0:
                    ans += dp(i,c,k-1)
               
            
            for i in range(c+1, len(pizza[0])):
                val = prefix[len(pizza)][i] + prefix[r][c] - prefix[r][i] - prefix[len(pizza)][c] > 0
                # print(val,r,c,i)
                if prefix[len(pizza)][i] + prefix[r][c] - prefix[r][i] - prefix[len(pizza)][c] > 0:
                    ans += dp(r,i,k-1)
                    # print(ans)
        
            return ans
        
        return dp(0,0,k) % 1000000007
            
            
            
            
            
            