class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            nums[i]= nums[i]*nums[i]
            i+=1
        nums.sort()
        return nums