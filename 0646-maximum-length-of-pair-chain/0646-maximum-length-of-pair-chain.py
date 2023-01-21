class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        
        @lru_cache(None)
        def dp(index, max_val):
            if index >= len(pairs): 
                return 0
            
            if pairs[index][0] > max_val:
                return max(1 + dp(index+1, pairs[index][1]),dp(index+1, max_val) )
            
            return dp(index + 1, max_val)
        
        return dp(0, -1001)
        