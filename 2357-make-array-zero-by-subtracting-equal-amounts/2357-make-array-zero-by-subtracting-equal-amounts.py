class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != 0 :
                break
        
        count = 0       
        bias = 0
        for j in range(i, len(nums)):
            if bias >= nums[-1]:
                return count
            if nums[j] > bias:
                bias += nums[j] - bias
                count += 1
        
        return count
            