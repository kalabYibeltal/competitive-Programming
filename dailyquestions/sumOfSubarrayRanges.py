class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum=0
        i=0
        while i < len(nums):
            j = i + 1
            maxx = minn = nums[i]
            while j < len(nums):
                if (nums[j]) > maxx:
                    maxx=nums[j]
                elif nums[j] < minn:
                    minn=nums[j]
                sum += (maxx-minn)
                j+=1
            i+=1
        return sum
                   
              
              
     
