class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left=1
        right=nums[-1]
        if len(nums)==1:
            return - (nums[0] // -threshold)
        while left<right:
            mid=(left+right)//2
            # print(mid)
            val= 0
            i=0
            while i < len(nums):
                val = val - (nums[i] // -mid)
                i+=1
            # print(val)
            if val > threshold:
                left=mid+1
                mid=(left+right)//2
                # print(0)
            else:
                right=mid
                # print(1)
                
        return mid
