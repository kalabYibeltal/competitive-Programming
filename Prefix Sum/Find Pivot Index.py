class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        su = 0
        for i in range(len(nums)):
            if su == (s - nums[i])/2: return i
            su += nums[i]
        return -1
  
# another trial
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         s = sum(nums)
#         r = 0
#         for i , num in enumerate(nums):
#             if r == s - num - r: return i 
#             r += num
            
#         return -1
