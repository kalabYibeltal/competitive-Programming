class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        total = ans = nums[1] - nums[0]
        a = 4
        
        for i in range(2,len(nums)):
            ans = 2 * ans + ((a-1)*( nums[i] - nums[i-1]))
            total += ans%1000000007
            a *= 2
        
        return total %1000000007