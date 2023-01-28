class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @lru_cache(None)
        def dp(l, r):
            if len(nums) - (r - l + 1) == len(multipliers) or l > r:
                return 0
            
            option1 = dp(l+1, r) + nums[l] * multipliers[len(nums) - (r - l + 1)]
            option2 = dp(l, r-1) + nums[r] * multipliers[len(nums) - (r - l + 1)]
            
            # print(option1, option2,)
            return max(option1, option2)
        
        return dp(0,len(nums)-1)