class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])
            
        @lru_cache(None)
        def dp(prev,i,count):
            if count == k and i == len(prefix):
                return 0
            if (count == k and  i != len(prefix)) or (count != k and i == len(prefix)):
                return -inf
                
            return max(dp(i,i+1,count + 1) + (( prefix[i] - prefix[prev]) / (i - prev)), dp(prev,i+1,count))
        
        return dp(0,1,0)