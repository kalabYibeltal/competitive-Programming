class Solution:
    def numberOfWays(self, s: str) -> int:
        
#         @lru_cache(None)
#         def dp(index, prev, count):
#             if count == 3:
#                 return 1
#             if index == len(s):
#                 return 0
            
#             if prev == s[index]:
#                 return dp(index+1, prev, count)
#             return dp(index+1, prev, count) + dp(index+1, s[index], count + 1)
        
#         return dp(0,-1,0)
            
    
        tzeros = tones = 0
        for i in s:
            if i == "1":
                tones += 1
            else:
                tzeros += 1
        
        zeros = ones = 0
        count = 0
        for i in s:
            if i == "1":
                count += zeros * (tzeros - zeros)
                ones += 1
            else:
                count += ones * (tones - ones)
                zeros += 1
        
        return count