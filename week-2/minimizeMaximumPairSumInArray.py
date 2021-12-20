class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        x=len(nums)/2
        y=len(nums)-1
        i=0
        max=0
        while(i<x):
            if nums[i]+nums[y-i]>max:
                max=nums[i]+nums[y-i]
            i+=1
        return max
