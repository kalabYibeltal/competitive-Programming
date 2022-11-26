class Solution:
    def countBits(self, n: int) -> List[int]:
        
        @lru_cache(None)
        def dp(n):
            if n ==1 or n == 0:
                return n
            
            else:
                return 1 + dp( int(bin(n)[3:], 2))
        
        answer = []
    
        for i in range(n+1):
            answer.append(dp(i))
        
        return answer
    