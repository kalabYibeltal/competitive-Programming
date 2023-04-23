class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        @lru_cache(None)
        def dp(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            
            num = ans =  0
            
            for i in range(index,len(s)):
                num = num * 10 + int(s[i])
                if num > k:
                    return ans% 1000000007
                
                ans += dp(i+1)
            
            return ans% 1000000007
        
            
        return dp(0) % 1000000007