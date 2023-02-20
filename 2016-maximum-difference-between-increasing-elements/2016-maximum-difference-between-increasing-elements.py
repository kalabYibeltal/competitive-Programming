class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        Max = -1
        Min = math.inf 
        for i in range(len(nums)):
            if Min > nums[i]:
                Min = nums[i]
            dif = nums[i] - Min 
            if Max < dif and dif != 0: 
                Max = dif
        return Max