class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        j = len(nums) - 1
        newarr = [0] * len(nums)
        for i in range(0,len(nums),2):
            newarr[i] = nums[j]
            j -= 1
        
        for i in range(1,len(nums),2):
            newarr[i] = nums[j]
            j -= 1
        
        return newarr