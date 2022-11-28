class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        for i in range(len(nums)+1):
            val = val ^ i
        
        for i in nums:
            val = val ^ i
        
        return val