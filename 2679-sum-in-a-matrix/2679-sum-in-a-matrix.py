class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        total = 0
        for arr in nums:
            arr.sort()
        for index in range(len(nums[0])-1,-1,-1):
            maxim = 0
            for jndex in range(len(nums)):
                maxim = max(maxim, nums[jndex][index])
            total += maxim
        
        return total