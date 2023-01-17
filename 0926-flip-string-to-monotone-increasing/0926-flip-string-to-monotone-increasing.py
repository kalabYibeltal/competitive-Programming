class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(bol, index):
            if index == len(s):
                return 0
            if bol:
                if s[index] == "1":
                    return dp(bol, index +1)
                else:
                    return 1 + dp(bol, index + 1)
            else:
                if s[index] == '1':
                    return min(1 + dp(bol, index + 1), dp(True, index + 1))
                else:
                    return dp(bol, index + 1)
        
        return dp(False, 0)