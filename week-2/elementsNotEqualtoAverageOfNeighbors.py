class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        n=len(nums)
        if(n%2 != 0):
            if(n<4):
                nums[0],nums[1]=nums[1],nums[0]
                return nums
            while(i<len(nums)-1):
                nums[i],nums[i+1]=nums[i+1],nums[i]
                i+=2
        if(n%2 == 0):
            while(i<len(nums)):
                nums[i],nums[i+1]=nums[i+1],nums[i]
                i+=2
        return nums
