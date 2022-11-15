class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #space = o(n) time nlong
        nums.sort()
        new_nums = [0] * len(nums)
        i = len(nums)-1 
        for j in range(1,len(new_nums),2):
            new_nums[j] = nums[i]
            i -= 1
        

        for j in range(0,len(new_nums),2):
            new_nums[j] = nums[i]
            i -= 1
        
        for i in range(len(nums)):
            nums[i] = new_nums[i]