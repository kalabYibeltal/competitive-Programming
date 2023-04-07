class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dic = defaultdict(int)
        for l,r,p in prices:
            dic[(l,r)] = p
        
        @lru_cache(None)
        def dp(m,n):
            if m == 0 or n == 0:
                return 0
            
            ans = dic[(m,n)]
            for i in range(1,m):
                ans = max(dp(i,n) + dp(m-i,n),ans)
                
            for j in range(1,n):
                ans = max(dp(m,j) + dp(m,n-j), ans)
                
                # print(dic[(i,n)], i , n, m)
            
            return ans
        
        return dp(m,n)